# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: build.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import common_pb2 as common__pb2
import step_pb2 as step__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='build.proto',
    package='buildbucket.v2',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x0b\x62uild.proto\x12\x0e\x62uildbucket.v2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0c\x63ommon.proto\x1a\nstep.proto\"\xf4\x07\n\x05\x42uild\x12\n\n\x02id\x18\x01 \x01(\x03\x12*\n\x07\x62uilder\x18\x02 \x01(\x0b\x32\x19.buildbucket.v2.BuilderID\x12\x0e\n\x06number\x18\x03 \x01(\x05\x12\x12\n\ncreated_by\x18\x04 \x01(\t\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x06status\x18\x0c \x01(\x0e\x32\x16.buildbucket.v2.Status\x12\x42\n\x14infra_failure_reason\x18\r \x01(\x0b\x32\".buildbucket.v2.InfraFailureReasonH\x00\x12\x35\n\rcancel_reason\x18\x0e \x01(\x0b\x32\x1c.buildbucket.v2.CancelReasonH\x00\x12*\n\x05input\x18\x0f \x01(\x0b\x32\x1b.buildbucket.v2.Build.Input\x12,\n\x06output\x18\x10 \x01(\x0b\x32\x1c.buildbucket.v2.Build.Output\x12#\n\x05steps\x18\x11 \x03(\x0b\x32\x14.buildbucket.v2.Step\x12)\n\x05infra\x18\x12 \x01(\x0b\x32\x1a.buildbucket.v2.BuildInfra\x12(\n\x04tags\x18\x13 \x03(\x0b\x32\x1a.buildbucket.v2.StringPair\x1a\xb7\x01\n\x05Input\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x35\n\x0egitiles_commit\x18\x02 \x01(\x0b\x32\x1d.buildbucket.v2.GitilesCommit\x12\x34\n\x0egerrit_changes\x18\x03 \x03(\x0b\x32\x1c.buildbucket.v2.GerritChange\x12\x14\n\x0c\x65xperimental\x18\x05 \x01(\x08\x1a\x86\x01\n\x06Output\x12+\n\nproperties\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x18\n\x10summary_markdown\x18\x02 \x01(\t\x12\x35\n\x0egitiles_commit\x18\x03 \x01(\x0b\x32\x1d.buildbucket.v2.GitilesCommitB\x0f\n\rstatus_reasonJ\x04\x08\x05\x10\x06\"4\n\x0c\x43\x61ncelReason\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61nceled_by\x18\x02 \x01(\t\"B\n\x12InfraFailureReason\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1b\n\x13resource_exhaustion\x18\x02 \x01(\x08\"\xf9\x03\n\nBuildInfra\x12;\n\x0b\x62uildbucket\x18\x01 \x01(\x0b\x32&.buildbucket.v2.BuildInfra.Buildbucket\x12\x35\n\x08swarming\x18\x02 \x01(\x0b\x32#.buildbucket.v2.BuildInfra.Swarming\x12\x31\n\x06logdog\x18\x03 \x01(\x0b\x32!.buildbucket.v2.BuildInfra.LogDog\x1a>\n\x0b\x42uildbucket\x12\x1f\n\x17service_config_revision\x18\x02 \x01(\t\x12\x0e\n\x06\x63\x61nary\x18\x04 \x01(\x08\x1a\xc6\x01\n\x08Swarming\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x0f\n\x07task_id\x18\x02 \x01(\t\x12\x1c\n\x14task_service_account\x18\x03 \x01(\t\x12\x10\n\x08priority\x18\x04 \x01(\x05\x12\x33\n\x0ftask_dimensions\x18\x05 \x03(\x0b\x32\x1a.buildbucket.v2.StringPair\x12\x32\n\x0e\x62ot_dimensions\x18\x06 \x03(\x0b\x32\x1a.buildbucket.v2.StringPair\x1a;\n\x06LogDog\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0e\n\x06prefix\x18\x03 \x01(\t\"=\n\tBuilderID\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x0f\n\x07\x62uilder\x18\x03 \x01(\tB6Z4go.chromium.org/luci/buildbucket/proto;buildbucketpbb\x06proto3'
    ),
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        common__pb2.DESCRIPTOR,
        step__pb2.DESCRIPTOR,
    ]
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BUILD_INPUT = _descriptor.Descriptor(
    name='Input',
    full_name='buildbucket.v2.Build.Input',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='properties',
            full_name='buildbucket.v2.Build.Input.properties',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='gitiles_commit',
            full_name='buildbucket.v2.Build.Input.gitiles_commit',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='gerrit_changes',
            full_name='buildbucket.v2.Build.Input.gerrit_changes',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='experimental',
            full_name='buildbucket.v2.Build.Input.experimental',
            index=3,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=790,
    serialized_end=973,
)

_BUILD_OUTPUT = _descriptor.Descriptor(
    name='Output',
    full_name='buildbucket.v2.Build.Output',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='properties',
            full_name='buildbucket.v2.Build.Output.properties',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='summary_markdown',
            full_name='buildbucket.v2.Build.Output.summary_markdown',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='gitiles_commit',
            full_name='buildbucket.v2.Build.Output.gitiles_commit',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=976,
    serialized_end=1110,
)

_BUILD = _descriptor.Descriptor(
    name='Build',
    full_name='buildbucket.v2.Build',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id',
            full_name='buildbucket.v2.Build.id',
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='builder',
            full_name='buildbucket.v2.Build.builder',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='number',
            full_name='buildbucket.v2.Build.number',
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='created_by',
            full_name='buildbucket.v2.Build.created_by',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='create_time',
            full_name='buildbucket.v2.Build.create_time',
            index=4,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='start_time',
            full_name='buildbucket.v2.Build.start_time',
            index=5,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='end_time',
            full_name='buildbucket.v2.Build.end_time',
            index=6,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='update_time',
            full_name='buildbucket.v2.Build.update_time',
            index=7,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='status',
            full_name='buildbucket.v2.Build.status',
            index=8,
            number=12,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='infra_failure_reason',
            full_name='buildbucket.v2.Build.infra_failure_reason',
            index=9,
            number=13,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='cancel_reason',
            full_name='buildbucket.v2.Build.cancel_reason',
            index=10,
            number=14,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='input',
            full_name='buildbucket.v2.Build.input',
            index=11,
            number=15,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='output',
            full_name='buildbucket.v2.Build.output',
            index=12,
            number=16,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='steps',
            full_name='buildbucket.v2.Build.steps',
            index=13,
            number=17,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='infra',
            full_name='buildbucket.v2.Build.infra',
            index=14,
            number=18,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='tags',
            full_name='buildbucket.v2.Build.tags',
            index=15,
            number=19,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[
        _BUILD_INPUT,
        _BUILD_OUTPUT,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='status_reason',
            full_name='buildbucket.v2.Build.status_reason',
            index=0,
            containing_type=None,
            fields=[]
        ),
    ],
    serialized_start=121,
    serialized_end=1133,
)

_CANCELREASON = _descriptor.Descriptor(
    name='CancelReason',
    full_name='buildbucket.v2.CancelReason',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='message',
            full_name='buildbucket.v2.CancelReason.message',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='canceled_by',
            full_name='buildbucket.v2.CancelReason.canceled_by',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1135,
    serialized_end=1187,
)

_INFRAFAILUREREASON = _descriptor.Descriptor(
    name='InfraFailureReason',
    full_name='buildbucket.v2.InfraFailureReason',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='message',
            full_name='buildbucket.v2.InfraFailureReason.message',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='resource_exhaustion',
            full_name='buildbucket.v2.InfraFailureReason.resource_exhaustion',
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1189,
    serialized_end=1255,
)

_BUILDINFRA_BUILDBUCKET = _descriptor.Descriptor(
    name='Buildbucket',
    full_name='buildbucket.v2.BuildInfra.Buildbucket',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='service_config_revision',
            full_name=
            'buildbucket.v2.BuildInfra.Buildbucket.service_config_revision',
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='canary',
            full_name='buildbucket.v2.BuildInfra.Buildbucket.canary',
            index=1,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1439,
    serialized_end=1501,
)

_BUILDINFRA_SWARMING = _descriptor.Descriptor(
    name='Swarming',
    full_name='buildbucket.v2.BuildInfra.Swarming',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='hostname',
            full_name='buildbucket.v2.BuildInfra.Swarming.hostname',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='task_id',
            full_name='buildbucket.v2.BuildInfra.Swarming.task_id',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='task_service_account',
            full_name='buildbucket.v2.BuildInfra.Swarming.task_service_account',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='priority',
            full_name='buildbucket.v2.BuildInfra.Swarming.priority',
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='task_dimensions',
            full_name='buildbucket.v2.BuildInfra.Swarming.task_dimensions',
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='bot_dimensions',
            full_name='buildbucket.v2.BuildInfra.Swarming.bot_dimensions',
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1504,
    serialized_end=1702,
)

_BUILDINFRA_LOGDOG = _descriptor.Descriptor(
    name='LogDog',
    full_name='buildbucket.v2.BuildInfra.LogDog',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='hostname',
            full_name='buildbucket.v2.BuildInfra.LogDog.hostname',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='project',
            full_name='buildbucket.v2.BuildInfra.LogDog.project',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='prefix',
            full_name='buildbucket.v2.BuildInfra.LogDog.prefix',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1704,
    serialized_end=1763,
)

_BUILDINFRA = _descriptor.Descriptor(
    name='BuildInfra',
    full_name='buildbucket.v2.BuildInfra',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='buildbucket',
            full_name='buildbucket.v2.BuildInfra.buildbucket',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='swarming',
            full_name='buildbucket.v2.BuildInfra.swarming',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='logdog',
            full_name='buildbucket.v2.BuildInfra.logdog',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[
        _BUILDINFRA_BUILDBUCKET,
        _BUILDINFRA_SWARMING,
        _BUILDINFRA_LOGDOG,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1258,
    serialized_end=1763,
)

_BUILDERID = _descriptor.Descriptor(
    name='BuilderID',
    full_name='buildbucket.v2.BuilderID',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='project',
            full_name='buildbucket.v2.BuilderID.project',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='bucket',
            full_name='buildbucket.v2.BuilderID.bucket',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
        _descriptor.FieldDescriptor(
            name='builder',
            full_name='buildbucket.v2.BuilderID.builder',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=1765,
    serialized_end=1826,
)

_BUILD_INPUT.fields_by_name[
    'properties'
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BUILD_INPUT.fields_by_name['gitiles_commit'
                           ].message_type = common__pb2._GITILESCOMMIT
_BUILD_INPUT.fields_by_name['gerrit_changes'
                           ].message_type = common__pb2._GERRITCHANGE
_BUILD_INPUT.containing_type = _BUILD
_BUILD_OUTPUT.fields_by_name[
    'properties'
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BUILD_OUTPUT.fields_by_name['gitiles_commit'
                            ].message_type = common__pb2._GITILESCOMMIT
_BUILD_OUTPUT.containing_type = _BUILD
_BUILD.fields_by_name['builder'].message_type = _BUILDERID
_BUILD.fields_by_name[
    'create_time'
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILD.fields_by_name[
    'start_time'
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILD.fields_by_name[
    'end_time'
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILD.fields_by_name[
    'update_time'
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILD.fields_by_name['status'].enum_type = common__pb2._STATUS
_BUILD.fields_by_name['infra_failure_reason'].message_type = _INFRAFAILUREREASON
_BUILD.fields_by_name['cancel_reason'].message_type = _CANCELREASON
_BUILD.fields_by_name['input'].message_type = _BUILD_INPUT
_BUILD.fields_by_name['output'].message_type = _BUILD_OUTPUT
_BUILD.fields_by_name['steps'].message_type = step__pb2._STEP
_BUILD.fields_by_name['infra'].message_type = _BUILDINFRA
_BUILD.fields_by_name['tags'].message_type = common__pb2._STRINGPAIR
_BUILD.oneofs_by_name['status_reason'].fields.append(
    _BUILD.fields_by_name['infra_failure_reason']
)
_BUILD.fields_by_name['infra_failure_reason'
                     ].containing_oneof = _BUILD.oneofs_by_name['status_reason']
_BUILD.oneofs_by_name['status_reason'].fields.append(
    _BUILD.fields_by_name['cancel_reason']
)
_BUILD.fields_by_name['cancel_reason'
                     ].containing_oneof = _BUILD.oneofs_by_name['status_reason']
_BUILDINFRA_BUILDBUCKET.containing_type = _BUILDINFRA
_BUILDINFRA_SWARMING.fields_by_name['task_dimensions'
                                   ].message_type = common__pb2._STRINGPAIR
_BUILDINFRA_SWARMING.fields_by_name['bot_dimensions'
                                   ].message_type = common__pb2._STRINGPAIR
_BUILDINFRA_SWARMING.containing_type = _BUILDINFRA
_BUILDINFRA_LOGDOG.containing_type = _BUILDINFRA
_BUILDINFRA.fields_by_name['buildbucket'].message_type = _BUILDINFRA_BUILDBUCKET
_BUILDINFRA.fields_by_name['swarming'].message_type = _BUILDINFRA_SWARMING
_BUILDINFRA.fields_by_name['logdog'].message_type = _BUILDINFRA_LOGDOG
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
DESCRIPTOR.message_types_by_name['CancelReason'] = _CANCELREASON
DESCRIPTOR.message_types_by_name['InfraFailureReason'] = _INFRAFAILUREREASON
DESCRIPTOR.message_types_by_name['BuildInfra'] = _BUILDINFRA
DESCRIPTOR.message_types_by_name['BuilderID'] = _BUILDERID

Build = _reflection.GeneratedProtocolMessageType(
    'Build',
    (_message.Message,),
    dict(
        Input=_reflection.GeneratedProtocolMessageType(
            'Input',
            (_message.Message,),
            dict(
                DESCRIPTOR=_BUILD_INPUT,
                __module__='build_pb2'
                # @@protoc_insertion_point(class_scope:buildbucket.v2.Build.Input)
            )
        ),
        Output=_reflection.GeneratedProtocolMessageType(
            'Output',
            (_message.Message,),
            dict(
                DESCRIPTOR=_BUILD_OUTPUT,
                __module__='build_pb2'
                # @@protoc_insertion_point(class_scope:buildbucket.v2.Build.Output)
            )
        ),
        DESCRIPTOR=_BUILD,
        __module__='build_pb2'
        # @@protoc_insertion_point(class_scope:buildbucket.v2.Build)
    )
)
_sym_db.RegisterMessage(Build)
_sym_db.RegisterMessage(Build.Input)
_sym_db.RegisterMessage(Build.Output)

CancelReason = _reflection.GeneratedProtocolMessageType(
    'CancelReason',
    (_message.Message,),
    dict(
        DESCRIPTOR=_CANCELREASON,
        __module__='build_pb2'
        # @@protoc_insertion_point(class_scope:buildbucket.v2.CancelReason)
    )
)
_sym_db.RegisterMessage(CancelReason)

InfraFailureReason = _reflection.GeneratedProtocolMessageType(
    'InfraFailureReason',
    (_message.Message,),
    dict(
        DESCRIPTOR=_INFRAFAILUREREASON,
        __module__='build_pb2'
        # @@protoc_insertion_point(class_scope:buildbucket.v2.InfraFailureReason)
    )
)
_sym_db.RegisterMessage(InfraFailureReason)

BuildInfra = _reflection.GeneratedProtocolMessageType(
    'BuildInfra',
    (_message.Message,),
    dict(
        Buildbucket=_reflection.GeneratedProtocolMessageType(
            'Buildbucket',
            (_message.Message,),
            dict(
                DESCRIPTOR=_BUILDINFRA_BUILDBUCKET,
                __module__='build_pb2'
                # @@protoc_insertion_point(class_scope:buildbucket.v2.BuildInfra.Buildbucket)
            )
        ),
        Swarming=_reflection.GeneratedProtocolMessageType(
            'Swarming',
            (_message.Message,),
            dict(
                DESCRIPTOR=_BUILDINFRA_SWARMING,
                __module__='build_pb2'
                # @@protoc_insertion_point(class_scope:buildbucket.v2.BuildInfra.Swarming)
            )
        ),
        LogDog=_reflection.GeneratedProtocolMessageType(
            'LogDog',
            (_message.Message,),
            dict(
                DESCRIPTOR=_BUILDINFRA_LOGDOG,
                __module__='build_pb2'
                # @@protoc_insertion_point(class_scope:buildbucket.v2.BuildInfra.LogDog)
            )
        ),
        DESCRIPTOR=_BUILDINFRA,
        __module__='build_pb2'
        # @@protoc_insertion_point(class_scope:buildbucket.v2.BuildInfra)
    )
)
_sym_db.RegisterMessage(BuildInfra)
_sym_db.RegisterMessage(BuildInfra.Buildbucket)
_sym_db.RegisterMessage(BuildInfra.Swarming)
_sym_db.RegisterMessage(BuildInfra.LogDog)

BuilderID = _reflection.GeneratedProtocolMessageType(
    'BuilderID',
    (_message.Message,),
    dict(
        DESCRIPTOR=_BUILDERID,
        __module__='build_pb2'
        # @@protoc_insertion_point(class_scope:buildbucket.v2.BuilderID)
    )
)
_sym_db.RegisterMessage(BuilderID)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b('Z4go.chromium.org/luci/buildbucket/proto;buildbucketpb')
)
# @@protoc_insertion_point(module_scope)
