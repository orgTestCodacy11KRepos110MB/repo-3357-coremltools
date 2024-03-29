#  Copyright (c) 2020, Apple Inc. All rights reserved.
#
#  Use of this source code is governed by a BSD-3-clause license that can be
#  found in the LICENSE.txt file or at https://opensource.org/licenses/BSD-3-Clause

import itertools

import numpy as np
import pytest

from coremltools.converters.mil import testing_reqs
from coremltools.converters.mil.mil import Builder as mb
from coremltools.converters.mil.mil.types import numpy_type_to_builtin_type
from coremltools.converters.mil.testing_utils import (
    apply_pass_and_basic_check, assert_model_is_valid, get_op_types_in_program)

np.random.seed(1984)

backends = testing_reqs.backends


def _apply_weight_transform(inputs, is_deconv, dtype=np.float32):
    """
    Utility funtion to test the weight transform function in conv batch_norm fusion pass.
    """
    Cin, _, groups = 10, 20, 10
    input_shape = (1, Cin, 2, 2)

    @mb.program(input_specs=[mb.TensorSpec(shape=input_shape, dtype=numpy_type_to_builtin_type(dtype))])
    def prog(x):

        if is_deconv:
            x = mb.conv_transpose(
                x=x,
                weight=inputs["conv_weight"],
                bias=inputs["conv_bias"],
                groups=groups,
            )
        else:
            x = mb.conv(
                x=x,
                weight=inputs["conv_weight"],
                bias=inputs["conv_bias"],
                groups=groups,
            )

        x = mb.batch_norm(
            x=x,
            mean=inputs["mean"],
            variance=inputs["variance"],
            gamma=inputs["gamma"],
            beta=inputs["beta"],
            epsilon=inputs["epsilon"],
        )
        return x

    apply_pass_and_basic_check(
        prog, "common::fuse_conv_batchnorm"
    )

    # get the updated weight from the prog
    conv_op = []
    for op in prog["main"].operations:
        if op.op_type == "const":
            continue
        conv_op.append(op)
    assert len(conv_op) == 1, "should only have one conv / conv_transpose layer."

    return conv_op[0].weight.val, conv_op[0].bias.val


class TestConvBatchNormOptimizationPasses:

    @pytest.mark.parametrize(
        "conv_type",
        ["conv", "conv_transpose"],
    )
    def test_weight_transform_conv_identity(self, conv_type):
        """
        Test the weight transform function with an identity batchnorm layer.
        """
        # parameters for conv
        is_deconv = conv_type == "conv_transpose"
        conv_weight = np.arange(20).astype(np.float32)
        conv_weight = np.reshape(conv_weight, (10, 2, 1, 1)) if is_deconv else np.reshape(conv_weight, (20, 1, 1, 1))
        conv_bias = np.arange(20).astype(np.float32)

        # parameters for batch_norm
        gamma = np.ones(20).astype(np.float32)
        beta = np.zeros(20).astype(np.float32)
        mean = np.zeros(20).astype(np.float32)
        variance = np.ones(20).astype(np.float32)
        epsilon = 0.

        inputs = {
            "conv_weight": conv_weight,
            "conv_bias": conv_bias,
            "gamma": gamma,
            "beta": beta,
            "mean": mean,
            "variance": variance,
            "epsilon": epsilon,
        }

        new_conv_weight, new_conv_bias = _apply_weight_transform(inputs, is_deconv)

        np.testing.assert_equal(new_conv_weight, conv_weight)
        np.testing.assert_equal(new_conv_bias, conv_bias)

    @pytest.mark.parametrize(
        "conv_type, dtype",
        itertools.product(
            ["conv", "conv_transpose"],
            [np.float16, np.float32],
        ),
    )
    def test_weight_transform_conv_type(self, conv_type, dtype):
        """
        The weight transform function should return an updated conv weight with correct data type
        """
        # parameters for conv
        is_deconv = conv_type == "conv_transpose"
        conv_weight = np.arange(20).astype(dtype)
        conv_weight = np.reshape(conv_weight, (10, 2, 1, 1)) if is_deconv else np.reshape(conv_weight, (20, 1, 1, 1))
        conv_bias = np.arange(20).astype(dtype)

        # parameters for batch_norm
        gamma = np.ones(20).astype(dtype)
        beta = np.zeros(20).astype(dtype)
        mean = np.zeros(20).astype(dtype)
        variance = np.ones(20).astype(dtype)
        epsilon = dtype(0.1)

        inputs = {
            "conv_weight": conv_weight,
            "conv_bias": conv_bias,
            "gamma": gamma,
            "beta": beta,
            "mean": mean,
            "variance": variance,
            "epsilon": epsilon,
        }

        new_conv_weight, _ = _apply_weight_transform(inputs, is_deconv, dtype)

        assert new_conv_weight.dtype == dtype, "the weight transform function should retain the weight's original dtype."

    @pytest.mark.parametrize(
        "rank, groups, has_bias, backend",
        itertools.product([3, 4, 5], [1, 2, 10], [False, True], backends),
    )
    def test_conv(self, rank, groups, has_bias, backend):
        """
        Input graph:
        input -----> conv -----> batch_norm ---> out

        Output graph:
        input -----> conv ----> out

        Different `rank` represents different conv dimensions: rank=3 for Conv1d, rank=4 for Conv2d, rank=5 for Conv3d.
        """
        Cin, Cout = 10, 30
        rank_to_input_shape = {3: (2, Cin, 20), 4: (2, Cin, 20, 24), 5: (2, Cin, 20, 24, 24)}
        rank_to_conv_weight_shape = {3: (Cout, Cin // groups, 2), 4: (Cout, Cin // groups, 2, 3),
                                     5: (Cout, Cin // groups, 2, 3, 3)}
        rank_to_output_shape = {3: (2, Cout, 19), 4: (2, Cout, 19, 22), 5: (2, Cout, 19, 22, 22)}

        input_shape = rank_to_input_shape[rank]

        @mb.program(input_specs=[mb.TensorSpec(shape=input_shape)])
        def prog(x):
            # conv layer
            conv_weight = np.random.rand(*rank_to_conv_weight_shape[rank])
            conv_bias = np.random.rand(Cout) if has_bias else None
            x = mb.conv(
                x=x,
                weight=conv_weight,
                bias=conv_bias,
                groups=groups,
            )

            # batch_norm layer
            gamma = np.random.rand(Cout)
            beta = np.random.rand(Cout)
            mean = np.random.rand(Cout)
            variance = np.random.rand(Cout)
            epsilon = 1e-2
            x = mb.batch_norm(
                x=x,
                mean=mean,
                variance=variance,
                gamma=gamma,
                beta=beta,
                epsilon=epsilon,
            )
            return x

        prev_prog, prev_block, block = apply_pass_and_basic_check(
            prog, "common::fuse_conv_batchnorm"
        )

        assert get_op_types_in_program(prev_prog) == ["conv", "batch_norm"]
        assert get_op_types_in_program(prog) == ["conv"]

        # validate graph pass
        output_shape = rank_to_output_shape[rank]
        assert_model_is_valid(
            prog,
            {"x": input_shape},
            expected_output_shapes={block.outputs[0].name: output_shape},
            backend=backend,
        )

    @pytest.mark.parametrize(
        "rank, groups, has_bias, backend",
        itertools.product([3, 4, 5], [1, 2, 10], [False, True], backends),
    )
    def test_conv_transpose(self, rank, groups, has_bias, backend):
        """
        Input graph:
        input -----> conv_transpose -----> batch_norm ---> out

        Output graph:
        input -----> conv_transpose ----> out
        """
        Cin, Cout = 10, 30
        rank_to_input_shape = {3: (2, Cin, 20), 4: (2, Cin, 20, 24), 5: (2, Cin, 20, 24, 24)}
        rank_to_conv_weight_shape = {3: (Cin, Cout // groups, 2), 4: (Cin, Cout // groups, 2, 3),
                                     5: (Cin, Cout // groups, 2, 3, 3)}
        rank_to_output_shape = {3: (2, Cout, 21), 4: (2, Cout, 21, 26), 5: (2, Cout, 21, 26, 26)}

        input_shape = rank_to_input_shape[rank]

        @mb.program(input_specs=[mb.TensorSpec(shape=input_shape)])
        def prog(x):
            # conv layer
            conv_weight = np.random.rand(*rank_to_conv_weight_shape[rank])
            conv_bias = np.random.rand(Cout) if has_bias else None
            x = mb.conv_transpose(
                x=x,
                weight=conv_weight,
                bias=conv_bias,
                groups=groups,
            )

            # batch_norm layer
            gamma = np.random.rand(Cout)
            beta = np.random.rand(Cout)
            mean = np.random.rand(Cout)
            variance = np.random.rand(Cout)

            epsilon = 1e-5
            x = mb.batch_norm(
                x=x,
                mean=mean,
                variance=variance,
                gamma=gamma,
                beta=beta,
                epsilon=epsilon,
            )
            return x

        prev_prog, prev_block, block = apply_pass_and_basic_check(
            prog, "common::fuse_conv_batchnorm"
        )

        assert get_op_types_in_program(prev_prog) == ["conv_transpose", "batch_norm"]
        assert get_op_types_in_program(prog) == ["conv_transpose"]

        # validate graph pass
        output_shape = rank_to_output_shape[rank]
        assert_model_is_valid(
            prog,
            {"x": input_shape},
            expected_output_shapes={block.outputs[0].name: output_shape},
            backend=backend,
        )
