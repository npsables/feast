"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import feast.core.DataSource_pb2
import feast.core.Feature_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FeatureTable(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SPEC_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def spec(self) -> global___FeatureTableSpec:
        """User-specified specifications of this feature table."""
        pass
    @property
    def meta(self) -> global___FeatureTableMeta:
        """System-populated metadata for this feature table."""
        pass
    def __init__(self,
        *,
        spec : typing.Optional[global___FeatureTableSpec] = ...,
        meta : typing.Optional[global___FeatureTableMeta] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta",b"meta","spec",b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["meta",b"meta","spec",b"spec"]) -> None: ...
global___FeatureTable = FeatureTable

class FeatureTableSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    ENTITIES_FIELD_NUMBER: builtins.int
    FEATURES_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MAX_AGE_FIELD_NUMBER: builtins.int
    BATCH_SOURCE_FIELD_NUMBER: builtins.int
    STREAM_SOURCE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the feature table. Must be unique. Not updated."""

    project: typing.Text = ...
    """Name of Feast project that this feature table belongs to."""

    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """List names of entities to associate with the Features defined in this 
        Feature Table. Not updatable.
        """
        pass
    @property
    def features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[feast.core.Feature_pb2.FeatureSpecV2]:
        """List of features specifications for each feature defined with this feature table."""
        pass
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """User defined metadata"""
        pass
    @property
    def max_age(self) -> google.protobuf.duration_pb2.Duration:
        """Features in this feature table can only be retrieved from online serving
        younger than max age. Age is measured as the duration of time between 
        the feature's event timestamp and when the feature is retrieved
        Feature values outside max age will be returned as unset values and indicated to end user
        """
        pass
    @property
    def batch_source(self) -> feast.core.DataSource_pb2.DataSource:
        """Batch/Offline DataSource to source batch/offline feature data.
        Only batch DataSource can be specified 
        (ie source type should start with 'BATCH_')
        """
        pass
    @property
    def stream_source(self) -> feast.core.DataSource_pb2.DataSource:
        """Stream/Online DataSource to source stream/online feature data.
        Only stream DataSource can be specified 
        (ie source type should start with 'STREAM_')
        """
        pass
    def __init__(self,
        *,
        name : typing.Text = ...,
        project : typing.Text = ...,
        entities : typing.Optional[typing.Iterable[typing.Text]] = ...,
        features : typing.Optional[typing.Iterable[feast.core.Feature_pb2.FeatureSpecV2]] = ...,
        labels : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        max_age : typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
        batch_source : typing.Optional[feast.core.DataSource_pb2.DataSource] = ...,
        stream_source : typing.Optional[feast.core.DataSource_pb2.DataSource] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["batch_source",b"batch_source","max_age",b"max_age","stream_source",b"stream_source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["batch_source",b"batch_source","entities",b"entities","features",b"features","labels",b"labels","max_age",b"max_age","name",b"name","project",b"project","stream_source",b"stream_source"]) -> None: ...
global___FeatureTableSpec = FeatureTableSpec

class FeatureTableMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATED_TIMESTAMP_FIELD_NUMBER: builtins.int
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    @property
    def created_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time where this Feature Table is created"""
        pass
    @property
    def last_updated_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time where this Feature Table is last updated"""
        pass
    revision: builtins.int = ...
    """Auto incrementing revision no. of this Feature Table"""

    hash: typing.Text = ...
    """Hash entities, features, batch_source and stream_source to inform JobService if
    jobs should be restarted should hash change
    """

    def __init__(self,
        *,
        created_timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_updated_timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        revision : builtins.int = ...,
        hash : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_timestamp",b"created_timestamp","last_updated_timestamp",b"last_updated_timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_timestamp",b"created_timestamp","hash",b"hash","last_updated_timestamp",b"last_updated_timestamp","revision",b"revision"]) -> None: ...
global___FeatureTableMeta = FeatureTableMeta