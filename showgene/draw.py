import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def draw_network_to_file(
    network_data: pd.DataFrame,
    save_path: str,
) -> None:
    """Draw a network to a file.

    Args:
        network_data: The network data.
        save_path: The path to save the network.
    """
    G = nx.Graph()

    for _, row in network_data.iterrows():
        node_A = row["preferredName_A"]
        node_B = row["preferredName_B"]
        weight = row["score"]
        G.add_edge(node_A, node_B, weight=weight)

    plt.style.use("ggplot")
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, width=1.0)

    plt.savefig(save_path, dpi=300, bbox_inches="tight")
