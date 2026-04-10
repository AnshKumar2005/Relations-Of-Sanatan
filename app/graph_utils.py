import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
import re


# =========================
# CHARACTER GRAPH
# =========================
def build_character_kg(name, index):
    name = name.strip().lower()

    if name not in index:
        return None

    G = nx.DiGraph()

    for s, r, o in index[name]:
        if s.lower() == name:
            G.add_node(s.capitalize(), type="character")
            G.add_node(o.capitalize())

            if "type" in r or "class" in r:
                G.add_edge(s.capitalize(), o.capitalize(), label="is-a")
            else:
                G.add_edge(s.capitalize(), o.capitalize(), label=r)

    return G


def character_graph_to_image(G):
    if G is None:
        return None

    pos = nx.spring_layout(G, k=0.7)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_axis_off()

    nx.draw_networkx_nodes(G, pos, node_size=2500, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=10, ax=ax)

    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=15, ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", ax=ax)

    buf = BytesIO()
    plt.savefig(buf, format="png", transparent=True)
    plt.close(fig)
    buf.seek(0)

    return Image.open(buf)


# =========================
# RELATION GRAPH
# =========================
def build_simple_relation_graph(char1, char2, relation_text):
    c1 = char1.capitalize()
    c2 = char2.capitalize()

    if "No direct relationship found" in relation_text:
        G = nx.DiGraph()
        G.add_node(c1)
        G.add_node(c2)
        return G

    relation = relation_text.replace(c1, "").replace(c2, "")
    relation = re.sub(r"[^\w\s]", "", relation)
    relation = relation.replace("is the", "").replace("is a", "").replace("was", "").strip()

    if relation == "":
        relation = "related to"

    G = nx.DiGraph()
    G.add_node(c1)
    G.add_node(c2)
    G.add_edge(c1, c2, label=relation)

    return G


def relation_graph_to_image(G):
    if G is None:
        return None

    nodes = list(G.nodes())
    if len(nodes) < 2:
        return None

    pos = {nodes[0]: (0, 0), nodes[1]: (4, 0)}

    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_axis_off()

    nx.draw_networkx_nodes(G, pos, node_size=3500, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=12, ax=ax)

    if len(G.edges()) > 0:
        nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, ax=ax)
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", ax=ax)

    buf = BytesIO()
    plt.savefig(buf, format="png", transparent=True)
    plt.close(fig)
    buf.seek(0)

    return Image.open(buf)