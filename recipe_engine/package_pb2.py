# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: package.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='package.proto',
  package='recipe_engine',
  syntax='proto2',
  serialized_pb=_b('\n\rpackage.proto\x12\rrecipe_engine\"\xbe\x01\n\x07\x44\x65pSpec\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x03 \x01(\t\x12\x10\n\x08revision\x18\x04 \x01(\t\x12\x15\n\rpath_override\x18\x05 \x01(\t\x12\x37\n\trepo_type\x18\x06 \x01(\x0e\x32\x1f.recipe_engine.DepSpec.RepoType:\x03GIT\" \n\x08RepoType\x12\x07\n\x03GIT\x10\x00\x12\x0b\n\x07GITILES\x10\x01\"\x8a\x01\n\x07Package\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\x05\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x14\n\x0crecipes_path\x18\x03 \x01(\t\x12\x1a\n\x12\x63\x61nonical_base_url\x18\x04 \x01(\t\x12$\n\x04\x64\x65ps\x18\x05 \x03(\x0b\x32\x16.recipe_engine.DepSpec')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DEPSPEC_REPOTYPE = _descriptor.EnumDescriptor(
  name='RepoType',
  full_name='recipe_engine.DepSpec.RepoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GITILES', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=191,
  serialized_end=223,
)
_sym_db.RegisterEnumDescriptor(_DEPSPEC_REPOTYPE)


_DEPSPEC = _descriptor.Descriptor(
  name='DepSpec',
  full_name='recipe_engine.DepSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='recipe_engine.DepSpec.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='recipe_engine.DepSpec.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='branch', full_name='recipe_engine.DepSpec.branch', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revision', full_name='recipe_engine.DepSpec.revision', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_override', full_name='recipe_engine.DepSpec.path_override', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repo_type', full_name='recipe_engine.DepSpec.repo_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEPSPEC_REPOTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=223,
)


_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='recipe_engine.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_version', full_name='recipe_engine.Package.api_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='recipe_engine.Package.project_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recipes_path', full_name='recipe_engine.Package.recipes_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='canonical_base_url', full_name='recipe_engine.Package.canonical_base_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deps', full_name='recipe_engine.Package.deps', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=364,
)

_DEPSPEC.fields_by_name['repo_type'].enum_type = _DEPSPEC_REPOTYPE
_DEPSPEC_REPOTYPE.containing_type = _DEPSPEC
_PACKAGE.fields_by_name['deps'].message_type = _DEPSPEC
DESCRIPTOR.message_types_by_name['DepSpec'] = _DEPSPEC
DESCRIPTOR.message_types_by_name['Package'] = _PACKAGE

DepSpec = _reflection.GeneratedProtocolMessageType('DepSpec', (_message.Message,), dict(
  DESCRIPTOR = _DEPSPEC,
  __module__ = 'package_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.DepSpec)
  ))
_sym_db.RegisterMessage(DepSpec)

Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), dict(
  DESCRIPTOR = _PACKAGE,
  __module__ = 'package_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.Package)
  ))
_sym_db.RegisterMessage(Package)


# @@protoc_insertion_point(module_scope)
