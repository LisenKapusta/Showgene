import io
from typing import List, Tuple

import pandas as pd
import requests

from showgene.constants import ENRICHMENT_URL, REQUEST_URL


def request_network_from_api(
    genes: List[str],
    species_id: int,
    node_count: int,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Request a network from the STRING API.

    Args:
        genes: The gene (or genes) name (names).
        species_id: The species ID from NBCI Database.
        node_count: The number of nodes.

    Returns:
        The network data and the enrichment data.
    """
    params = {
        "identifiers": "%0d".join(genes),
        "species": species_id,
        "add_white_nodes": node_count,
        "network_flavor": "confidence",
        "caller_identity": "showgene.app",
    }

    response = requests.get(REQUEST_URL, params=params)
    network_df = pd.read_csv(io.StringIO(response.text), sep="\t")

    response = requests.get(ENRICHMENT_URL, params=params)
    enrichment_df = pd.read_csv(io.StringIO(response.text), sep="\t")

    return network_df, enrichment_df
