# type: ignore[attr-defined]

from enum import Enum
from pathlib import Path

import typer
from dbt.contracts.graph.manifest import WritableManifest
from dbt.contracts.results import CatalogArtifact
from rich.console import Console

from dbt_subdocs import version
from dbt_subdocs.dtos import RemovableNodeType
from dbt_subdocs.usecase.edit_catalog import edit_catalog
from dbt_subdocs.usecase.edit_manifest import only_node_with_tags, remove_attribute


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="dbt-subdocs",
    help="dbt-subdocs is a python CLI you can used to generate a dbt-docs for a subset of your dbt project",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]dbt-subdocs[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command()
def main(
    directory: Path = typer.Option(
        Path.cwd(),
        help="the directory that contains the manifest.json and catalog.json",
        dir_okay=True,
        exists=True,
        file_okay=False,
        writable=True,
        readable=True,
    ),
    output_dir: Path = typer.Option(
        Path.cwd(),
        help="the output directory",
        dir_okay=True,
        writable=True,
        readable=True,
    ),
    tag: list[str] = typer.Option(
        [],
        help="the tags to keep in the doc",
    ),
    excluded_node_type: list[RemovableNodeType] = typer.Option(
        [], help="The root node to exclude", show_choices=True
    ),
) -> None:
    input_manifest_file = directory / "manifest.json"
    manifest = WritableManifest.read(input_manifest_file.as_posix())
    manifest = only_node_with_tags(manifest, tag)
    for node_type in excluded_node_type:
        manifest = remove_attribute(manifest, node_type)
    output_manifest_file = output_dir / "manifest.json"
    manifest.write(output_manifest_file.as_posix())

    input_catalog_file = directory / "catalog.json"
    catalog = CatalogArtifact.read(input_catalog_file.as_posix())
    catalog = edit_catalog(catalog, manifest)
    output_catalog_file = output_dir / "catalog.json"
    catalog.write(output_catalog_file.as_posix())


if __name__ == "__main__":
    app()
