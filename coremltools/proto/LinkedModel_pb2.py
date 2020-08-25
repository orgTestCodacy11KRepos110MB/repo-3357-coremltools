# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LinkedModel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Parameters_pb2 as Parameters__pb2
try:
  DataStructures__pb2 = Parameters__pb2.DataStructures__pb2
except AttributeError:
  DataStructures__pb2 = Parameters__pb2.DataStructures_pb2
try:
  FeatureTypes__pb2 = Parameters__pb2.FeatureTypes__pb2
except AttributeError:
  FeatureTypes__pb2 = Parameters__pb2.FeatureTypes_pb2

from .Parameters_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='LinkedModel.proto',
  package='CoreML.Specification',
  syntax='proto3',
  serialized_pb=_b('\n\x11LinkedModel.proto\x12\x14\x43oreML.Specification\x1a\x10Parameters.proto\"[\n\x0bLinkedModel\x12@\n\x0flinkedModelFile\x18\x01 \x01(\x0b\x32%.CoreML.Specification.LinkedModelFileH\x00\x42\n\n\x08LinkType\"\x9b\x01\n\x0fLinkedModelFile\x12\x42\n\x13linkedModelFileName\x18\x01 \x01(\x0b\x32%.CoreML.Specification.StringParameter\x12\x44\n\x15linkedModelSearchPath\x18\x02 \x01(\x0b\x32%.CoreML.Specification.StringParameterB\x02H\x03P\x00\x62\x06proto3')
  ,
  dependencies=[Parameters__pb2.DESCRIPTOR,],
  public_dependencies=[Parameters__pb2.DESCRIPTOR,])




_LINKEDMODEL = _descriptor.Descriptor(
  name='LinkedModel',
  full_name='CoreML.Specification.LinkedModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linkedModelFile', full_name='CoreML.Specification.LinkedModel.linkedModelFile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='LinkType', full_name='CoreML.Specification.LinkedModel.LinkType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=61,
  serialized_end=152,
)


_LINKEDMODELFILE = _descriptor.Descriptor(
  name='LinkedModelFile',
  full_name='CoreML.Specification.LinkedModelFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linkedModelFileName', full_name='CoreML.Specification.LinkedModelFile.linkedModelFileName', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linkedModelSearchPath', full_name='CoreML.Specification.LinkedModelFile.linkedModelSearchPath', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=310,
)

_LINKEDMODEL.fields_by_name['linkedModelFile'].message_type = _LINKEDMODELFILE
_LINKEDMODEL.oneofs_by_name['LinkType'].fields.append(
  _LINKEDMODEL.fields_by_name['linkedModelFile'])
_LINKEDMODEL.fields_by_name['linkedModelFile'].containing_oneof = _LINKEDMODEL.oneofs_by_name['LinkType']
_LINKEDMODELFILE.fields_by_name['linkedModelFileName'].message_type = Parameters__pb2._STRINGPARAMETER
_LINKEDMODELFILE.fields_by_name['linkedModelSearchPath'].message_type = Parameters__pb2._STRINGPARAMETER
DESCRIPTOR.message_types_by_name['LinkedModel'] = _LINKEDMODEL
DESCRIPTOR.message_types_by_name['LinkedModelFile'] = _LINKEDMODELFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinkedModel = _reflection.GeneratedProtocolMessageType('LinkedModel', (_message.Message,), dict(
  DESCRIPTOR = _LINKEDMODEL,
  __module__ = 'LinkedModel_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.LinkedModel)
  ))
_sym_db.RegisterMessage(LinkedModel)

LinkedModelFile = _reflection.GeneratedProtocolMessageType('LinkedModelFile', (_message.Message,), dict(
  DESCRIPTOR = _LINKEDMODELFILE,
  __module__ = 'LinkedModel_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.LinkedModelFile)
  ))
_sym_db.RegisterMessage(LinkedModelFile)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)