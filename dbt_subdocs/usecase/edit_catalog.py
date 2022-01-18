from copy import deepcopy

from dbt.contracts.graph.manifest import WritableManifest
from dbt.contracts.results import CatalogArtifact


def edit_catalog(
    catalog: CatalogArtifact, manifest: WritableManifest
) -> CatalogArtifact:
    output = deepcopy(catalog)
    node_names = tuple(node for node in output.nodes)
    for node in node_names:
        if node not in manifest.nodes:
            output.nodes.pop(node)
    source_names = tuple(source for source in output.sources)
    for source in source_names:
        if source not in manifest.sources:
            output.sources.pop(source)
    return output
