import argparse

from showgene.draw import draw_network_to_file
from showgene.request import request_network_from_api


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show a gene network from the STRING API.",
    )
    parser.add_argument(
        "-g",
        "--gene",
        type=str,
        required=True,
        help="The gene name.",
    )
    parser.add_argument(
        "-s",
        "--species_id",
        type=int,
        required=False,
        help="The species ID from NBCI Database. Defaults to 9606.",
        default=9606,
    )
    parser.add_argument(
        "-n",
        "--node_count",
        type=int,
        required=False,
        help="The number of nodes.",
        default=32,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=False,
        help="The output file path. Defaults to network.png.",
        default="network.png",
    )

    return parser.parse_args()


def show_gene_network(
    gene: str,
    species_id: int,
    node_count: int,
    output: str,
) -> None:
    """Show a gene network from the STRING API.

    Args:
        gene: The gene name.
        species_id: The species ID from NBCI Database.
        node_count: The number of nodes.
        output: The output file path.
    """
    df = request_network_from_api(
        gene=gene,
        species_id=species_id,
        node_count=node_count,
    )
    draw_network_to_file(df, output)


def main() -> None:
    """The main function."""
    args = parse_args()
    show_gene_network(
        gene=args.gene,
        species_id=args.species_id,
        node_count=args.node_count,
        output=args.output,
    )
