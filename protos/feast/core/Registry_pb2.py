# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/Registry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.protos.feast.core import Entity_pb2 as feast_dot_core_dot_Entity__pb2
from feast.protos.feast.core import FeatureService_pb2 as feast_dot_core_dot_FeatureService__pb2
from feast.protos.feast.core import FeatureTable_pb2 as feast_dot_core_dot_FeatureTable__pb2
from feast.protos.feast.core import FeatureView_pb2 as feast_dot_core_dot_FeatureView__pb2
from feast.protos.feast.core import InfraObject_pb2 as feast_dot_core_dot_InfraObject__pb2
from feast.protos.feast.core import OnDemandFeatureView_pb2 as feast_dot_core_dot_OnDemandFeatureView__pb2
from feast.protos.feast.core import RequestFeatureView_pb2 as feast_dot_core_dot_RequestFeatureView__pb2
from feast.protos.feast.core import StreamFeatureView_pb2 as feast_dot_core_dot_StreamFeatureView__pb2
from feast.protos.feast.core import DataSource_pb2 as feast_dot_core_dot_DataSource__pb2
from feast.protos.feast.core import SavedDataset_pb2 as feast_dot_core_dot_SavedDataset__pb2
from feast.protos.feast.core import ValidationProfile_pb2 as feast_dot_core_dot_ValidationProfile__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66\x65\x61st/core/Registry.proto\x12\nfeast.core\x1a\x17\x66\x65\x61st/core/Entity.proto\x1a\x1f\x66\x65\x61st/core/FeatureService.proto\x1a\x1d\x66\x65\x61st/core/FeatureTable.proto\x1a\x1c\x66\x65\x61st/core/FeatureView.proto\x1a\x1c\x66\x65\x61st/core/InfraObject.proto\x1a$feast/core/OnDemandFeatureView.proto\x1a#feast/core/RequestFeatureView.proto\x1a\"feast/core/StreamFeatureView.proto\x1a\x1b\x66\x65\x61st/core/DataSource.proto\x1a\x1d\x66\x65\x61st/core/SavedDataset.proto\x1a\"feast/core/ValidationProfile.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe6\x05\n\x08Registry\x12$\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x12.feast.core.Entity\x12\x30\n\x0e\x66\x65\x61ture_tables\x18\x02 \x03(\x0b\x32\x18.feast.core.FeatureTable\x12.\n\rfeature_views\x18\x06 \x03(\x0b\x32\x17.feast.core.FeatureView\x12,\n\x0c\x64\x61ta_sources\x18\x0c \x03(\x0b\x32\x16.feast.core.DataSource\x12@\n\x17on_demand_feature_views\x18\x08 \x03(\x0b\x32\x1f.feast.core.OnDemandFeatureView\x12=\n\x15request_feature_views\x18\t \x03(\x0b\x32\x1e.feast.core.RequestFeatureView\x12;\n\x14stream_feature_views\x18\x0e \x03(\x0b\x32\x1d.feast.core.StreamFeatureView\x12\x34\n\x10\x66\x65\x61ture_services\x18\x07 \x03(\x0b\x32\x1a.feast.core.FeatureService\x12\x30\n\x0esaved_datasets\x18\x0b \x03(\x0b\x32\x18.feast.core.SavedDataset\x12>\n\x15validation_references\x18\r \x03(\x0b\x32\x1f.feast.core.ValidationReference\x12 \n\x05infra\x18\n \x01(\x0b\x32\x11.feast.core.Infra\x12\x35\n\x10project_metadata\x18\x0f \x03(\x0b\x32\x1b.feast.core.ProjectMetadata\x12\x1f\n\x17registry_schema_version\x18\x03 \x01(\t\x12\x12\n\nversion_id\x18\x04 \x01(\t\x12\x30\n\x0clast_updated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\x0fProjectMetadata\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x14\n\x0cproject_uuid\x18\x02 \x01(\tBR\n\x10\x66\x65\x61st.proto.coreB\rRegistryProtoZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.core.Registry_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020feast.proto.coreB\rRegistryProtoZ/github.com/feast-dev/feast/go/protos/feast/core'
  _globals['_REGISTRY']._serialized_start=431
  _globals['_REGISTRY']._serialized_end=1173
  _globals['_PROJECTMETADATA']._serialized_start=1175
  _globals['_PROJECTMETADATA']._serialized_end=1231
# @@protoc_insertion_point(module_scope)