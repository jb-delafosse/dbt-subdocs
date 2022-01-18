from copy import deepcopy

from dbt.contracts.graph.manifest import WritableManifest

from dbt_subdocs.dtos import RemovableNodeType


def remove_attribute(
    manifest: WritableManifest, attribute: RemovableNodeType
) -> WritableManifest:
    output = deepcopy(manifest)
    output.__setattr__(attribute, {})
    return output


def only_node_with_tags(
    manifest: WritableManifest, tags: list[str]
) -> WritableManifest:
    node_names = [node for node in manifest.nodes]
    output = deepcopy(manifest)
    to_keep = {}
    for node_name in node_names:
        tags_present = list(tag in output.nodes[node_name].tags for tag in tags)
        if any(tags_present):
            to_keep[node_name] = output.nodes[node_name]
    output.nodes = to_keep
    return output
