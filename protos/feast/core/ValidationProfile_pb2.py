# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/ValidationProfile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"feast/core/ValidationProfile.proto\x12\nfeast.core\"\x83\x01\n\x14GEValidationProfiler\x12\x46\n\x08profiler\x18\x01 \x01(\x0b\x32\x34.feast.core.GEValidationProfiler.UserDefinedProfiler\x1a#\n\x13UserDefinedProfiler\x12\x0c\n\x04\x62ody\x18\x01 \x01(\x0c\"0\n\x13GEValidationProfile\x12\x19\n\x11\x65xpectation_suite\x18\x01 \x01(\x0c\"\xdd\x02\n\x13ValidationReference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16reference_dataset_name\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x37\n\x04tags\x18\x05 \x03(\x0b\x32).feast.core.ValidationReference.TagsEntry\x12\x37\n\x0bge_profiler\x18\x06 \x01(\x0b\x32 .feast.core.GEValidationProfilerH\x00\x12\x35\n\nge_profile\x18\x07 \x01(\x0b\x32\x1f.feast.core.GEValidationProfileH\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\n\n\x08profilerB\x10\n\x0e\x63\x61\x63hed_profileBV\n\x10\x66\x65\x61st.proto.coreB\x11ValidationProfileZ/github.com/feast-dev/feast/go/protos/feast/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.core.ValidationProfile_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020feast.proto.coreB\021ValidationProfileZ/github.com/feast-dev/feast/go/protos/feast/core'
  _VALIDATIONREFERENCE_TAGSENTRY._options = None
  _VALIDATIONREFERENCE_TAGSENTRY._serialized_options = b'8\001'
  _globals['_GEVALIDATIONPROFILER']._serialized_start=51
  _globals['_GEVALIDATIONPROFILER']._serialized_end=182
  _globals['_GEVALIDATIONPROFILER_USERDEFINEDPROFILER']._serialized_start=147
  _globals['_GEVALIDATIONPROFILER_USERDEFINEDPROFILER']._serialized_end=182
  _globals['_GEVALIDATIONPROFILE']._serialized_start=184
  _globals['_GEVALIDATIONPROFILE']._serialized_end=232
  _globals['_VALIDATIONREFERENCE']._serialized_start=235
  _globals['_VALIDATIONREFERENCE']._serialized_end=584
  _globals['_VALIDATIONREFERENCE_TAGSENTRY']._serialized_start=511
  _globals['_VALIDATIONREFERENCE_TAGSENTRY']._serialized_end=554
# @@protoc_insertion_point(module_scope)