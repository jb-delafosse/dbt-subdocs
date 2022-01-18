from enum import Enum


class RemovableNodeType(str, Enum):
    SOURCES = "sources"
    MACROS = "macros"
    EXPOSURES = "exposures"
    METRICS = "metrics"
    SELECTORS = "selectors"
    DISABLED = "disabled"
    PARENT_MAP = "parent_map"
    CHILD_MAP = "child_map"
    METADATA = "metadata"
