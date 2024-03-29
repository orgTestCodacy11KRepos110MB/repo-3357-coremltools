#  Copyright (c) 2020, Apple Inc. All rights reserved.
#
#  Use of this source code is governed by a BSD-3-clause license that can be
#  found in the LICENSE.txt file or at https://opensource.org/licenses/BSD-3-Clause

from coremltools import _logger as logger
from coremltools.converters.mil.mil.passes.pass_registry import PASS_REGISTRY


def nn_backend_passes(prog):
    passes = [
        "nn_backend::commingle_loop_vars",  # after loop_invariant_elimination
        "nn_backend::handle_return_inputs_as_outputs",
        "common::const_elimination",
        "common::dead_code_elimination",
        "nn_backend::handle_unused_inputs",  # must come after dce.
        "nn_backend::alert_return_type_cast",  # must be at the end.
    ]

    prog.validate()
    for p in passes:
        logger.info('Performing passes for nn_backend: "{}"'.format(p))
        PASS_REGISTRY[p](prog)
        # No more validation from this point on as prog is not SSA anymore.

    logger.debug("Program after nn backend passes:\n{}".format(prog))
