# type: ignore[attr-defined]
"""dbt-subdocs is a python CLI you can used to generate a dbt-docs for a subset of your dbt project"""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
