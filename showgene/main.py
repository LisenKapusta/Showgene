import argparse
from typing import List

from showgene.draw import draw_network_to_file
from showgene.request import request_network_from_api


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show a gene network from the STRING API.",
    )
    parser.add_argument(
        "-g",
        "--genes",
        type=str,
        required=True,
        help="The gene (or genes) name (names).",
        nargs="+",
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
        default=0,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=False,
        help="The output file path. Defaults to network.png.",
        default="network.png",
    )
    parser.add_argument(
        "-eo",
        "--enrichment_output",
        type=str,
        required=False,
        help="Enrichment output file path. Defaults to network_enrichment.csv.",
        default="network_enrichment.csv",
    )

    return parser.parse_args()


def show_gene_network(
    genes: List[str],
    species_id: int,
    node_count: int,
    output: str,
    enrichment_output: str,
) -> None:
    """Show a gene network from the STRING API.

    Args:
        genes: The gene (or genes) name (names).
        species_id: The species ID from NBCI Database.
        node_count: The number of nodes.
        output: The output file path.
        enrichment_output: Enrichment output file path.
    """
    network_df, enrichment_df = request_network_from_api(
        genes=genes,
        species_id=species_id,
        node_count=node_count,
    )
    enrichment_df.to_csv(enrichment_output, index=False)
    draw_network_to_file(network_df, output)


def main() -> None:
    """The main function."""
    args = parse_args()
    show_gene_network(
        genes=args.genes,
        species_id=args.species_id,
        node_count=args.node_count,
        output=args.output,
        enrichment_output=args.enrichment_output,
    )
