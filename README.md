# 🔱 Relations Of Sanatan

### AI-Powered Knowledge Graph for Hindu Mythology

---

## 🌟 Overview

**Relations Of Sanatan** is an AI-driven system that converts Hindu mythological data into a **structured knowledge graph**, enabling deep exploration of:

* 🧑 Characters
* 🤝 Relationships
* 📊 Graph structures

It combines **triplets + ontology (RDF/TTL) + graph visualization + reasoning logic** into an interactive interface.

---

## 🚀 Features

### 🧑 Character Explorer

* Generates structured descriptions
* Extracts:

  * Parents, spouses, children
  * Roles and identities
  * Kingdoms and teachers

---

### 🤝 Relationship Explorer

* Finds relationships between any two characters:

  * Direct → father, spouse, sibling
  * Indirect → uncle, aunt, in-law
  * Semantic → enemy, companion

---

### 📊 Knowledge Graph Visualization

* Built using NetworkX
* Dynamic relationship graphs

---

## 🏗️ Architecture

```
Raw Mythology Text
        ↓
Triplet Extraction (S-R-O)
        ↓
Ontology Mapping (TTL)
        ↓
Indexing + Logic
        ↓
Graph + UI (Gradio)
```

---

## 📂 Project Structure

```
MythoGraph/
│
├── app/
├── data/
├── assets/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation
1️⃣ Clone the repository
```bash
git clone https://github.com/AnshKumar2005/MythoGraph-A-Knowledge-Graph-of-Hindu-Mythology-for-Relationship-Exploration.git
cd MythoGraph
pip install -r requirements.txt
```
2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

---

## ▶️ Run

```bash
python app/main.py
```
---

📊 Example Use Cases
🔍 Character Query

Input:

Arjuna

Output:

Biography
Relationships
Knowledge graph
🔗 Relationship Query

Input:

Arjuna, Krishna

Output:

Krishna is the charioteer of Arjuna
Graph visualization

---

## 📚 Dataset

This project uses:

Custom triplets extracted from mythology texts
RDF ontology for semantic enrichment

🔗🔗 Dataset Repo:
 https://github.com/AnshKumar2005/MythoGraph-A-Knowledge-Graph-of-Hindu-Mythology-for-Relationship-Exploration

---

## 🧠 Tech Stack

* Python
* Gradio
* NetworkX
* RDFLib
* Knowledge Graphs
* Matplotlib
* Ontology (RDF/TTL)

---

## 🚀 Future Work

* Neo4j integration
* LLM-based reasoning
* Natural language queries
* Web deployment

---
📜 License

MIT License

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
