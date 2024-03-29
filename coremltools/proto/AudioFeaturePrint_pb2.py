# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AudioFeaturePrint.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AudioFeaturePrint.proto',
  package='CoreML.Specification.CoreMLModels',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x41udioFeaturePrint.proto\x12!CoreML.Specification.CoreMLModels\"\x9d\x02\n\x11\x41udioFeaturePrint\x12K\n\x05sound\x18\x14 \x01(\x0b\x32:.CoreML.Specification.CoreMLModels.AudioFeaturePrint.SoundH\x00\x1a\xa1\x01\n\x05Sound\x12X\n\x07version\x18\x01 \x01(\x0e\x32G.CoreML.Specification.CoreMLModels.AudioFeaturePrint.Sound.SoundVersion\">\n\x0cSoundVersion\x12\x19\n\x15SOUND_VERSION_INVALID\x10\x00\x12\x13\n\x0fSOUND_VERSION_1\x10\x01\x42\x17\n\x15\x41udioFeaturePrintTypeB\x02H\x03\x62\x06proto3')
)



_AUDIOFEATUREPRINT_SOUND_SOUNDVERSION = _descriptor.EnumDescriptor(
  name='SoundVersion',
  full_name='CoreML.Specification.CoreMLModels.AudioFeaturePrint.Sound.SoundVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SOUND_VERSION_INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUND_VERSION_1', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=261,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_AUDIOFEATUREPRINT_SOUND_SOUNDVERSION)


_AUDIOFEATUREPRINT_SOUND = _descriptor.Descriptor(
  name='Sound',
  full_name='CoreML.Specification.CoreMLModels.AudioFeaturePrint.Sound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='CoreML.Specification.CoreMLModels.AudioFeaturePrint.Sound.version', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUDIOFEATUREPRINT_SOUND_SOUNDVERSION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=323,
)

_AUDIOFEATUREPRINT = _descriptor.Descriptor(
  name='AudioFeaturePrint',
  full_name='CoreML.Specification.CoreMLModels.AudioFeaturePrint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sound', full_name='CoreML.Specification.CoreMLModels.AudioFeaturePrint.sound', index=0,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_AUDIOFEATUREPRINT_SOUND, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='AudioFeaturePrintType', full_name='CoreML.Specification.CoreMLModels.AudioFeaturePrint.AudioFeaturePrintType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=63,
  serialized_end=348,
)

_AUDIOFEATUREPRINT_SOUND.fields_by_name['version'].enum_type = _AUDIOFEATUREPRINT_SOUND_SOUNDVERSION
_AUDIOFEATUREPRINT_SOUND.containing_type = _AUDIOFEATUREPRINT
_AUDIOFEATUREPRINT_SOUND_SOUNDVERSION.containing_type = _AUDIOFEATUREPRINT_SOUND
_AUDIOFEATUREPRINT.fields_by_name['sound'].message_type = _AUDIOFEATUREPRINT_SOUND
_AUDIOFEATUREPRINT.oneofs_by_name['AudioFeaturePrintType'].fields.append(
  _AUDIOFEATUREPRINT.fields_by_name['sound'])
_AUDIOFEATUREPRINT.fields_by_name['sound'].containing_oneof = _AUDIOFEATUREPRINT.oneofs_by_name['AudioFeaturePrintType']
DESCRIPTOR.message_types_by_name['AudioFeaturePrint'] = _AUDIOFEATUREPRINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioFeaturePrint = _reflection.GeneratedProtocolMessageType('AudioFeaturePrint', (_message.Message,), dict(

  Sound = _reflection.GeneratedProtocolMessageType('Sound', (_message.Message,), dict(
    DESCRIPTOR = _AUDIOFEATUREPRINT_SOUND,
    __module__ = 'AudioFeaturePrint_pb2'
    # @@protoc_insertion_point(class_scope:CoreML.Specification.CoreMLModels.AudioFeaturePrint.Sound)
    ))
  ,
  DESCRIPTOR = _AUDIOFEATUREPRINT,
  __module__ = 'AudioFeaturePrint_pb2'
  # @@protoc_insertion_point(class_scope:CoreML.Specification.CoreMLModels.AudioFeaturePrint)
  ))
_sym_db.RegisterMessage(AudioFeaturePrint)
_sym_db.RegisterMessage(AudioFeaturePrint.Sound)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
