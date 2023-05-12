import io

import pandas as pd
import requests

from showgene.constants import REQUEST_URL


def request_network_from_api(
    gene: str,
    species_id: int,
    node_count: int,
) -> pd.DataFrame:
    """Request a network from the STRING API.

    Args:
        gene: The gene name.
        species_id: The species ID from NBCI Database.
        node_count: The number of nodes.

    Returns:
        A pandas DataFrame with the network.
    """

    params = {
        "identifiers": gene,
        "species": species_id,
        "add_white_nodes": node_count,
        "network_flavor": "confidence",
        "caller_identity": "showgene.app",
    }
    response = requests.get(REQUEST_URL, params=params)

    return pd.read_csv(io.StringIO(response.text), sep="\t")
