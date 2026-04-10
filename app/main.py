from app.graph_utils import (
    build_character_kg,
    character_graph_to_image,
    build_simple_relation_graph,
    relation_graph_to_image
)

from app.data_loader import load_all_data, index
from app.character import describe_character
from app.relationship import extract_relationship

import gradio as gr

# LOAD DATA
load_all_data()

def get_char(name):
    bio = describe_character(name)
    G = build_character_kg(name, index)
    img = character_graph_to_image(G)
    return bio, img

def get_rel(a, b):
    rel_text = extract_relationship(a, b)
    G = build_simple_relation_graph(a, b, rel_text)
    img = relation_graph_to_image(G)
    return rel_text, img

with gr.Blocks() as app:

    gr.Markdown("# 🔱 MythoGraph Explorer")

    with gr.Tab("Character"):
        name = gr.Textbox(label="Character")
        out = gr.Textbox(label="Description")
        img = gr.Image(label="Knowledge Graph")
        btn = gr.Button("Generate")
        btn.click(get_char, name, [out, img])

    with gr.Tab("Relationship"):
        a = gr.Textbox(label="Character 1")
        b = gr.Textbox(label="Character 2")
        out2 = gr.Textbox(label="Relationship")
        img2 = gr.Image(label="Graph")
        btn2 = gr.Button("Find")
        btn2.click(get_rel, [a, b], [out2, img2])

app.launch()