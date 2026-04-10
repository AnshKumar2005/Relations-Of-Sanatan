import re
from collections import defaultdict
from rdflib import Graph

TRIPLET_FILE = "data/triplets_curated.txt"
TTL_FILE = "data/triplets_formatted.ttl"

triplets = []
index = defaultdict(list)

parents_of = defaultdict(set)
children_of = defaultdict(set)
spouses_of = defaultdict(set)
siblings_of = defaultdict(set)
enemies_of = defaultdict(set)
charioteer_map = defaultdict(set)
actions = defaultdict(list)


def load_all_data():
    # =========================
    # LOAD TRIPLETS
    # =========================
    with open(TRIPLET_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("{"):
                continue

            parts = re.findall(r'"(.*?)"', line)
            if len(parts) == 3:
                s, r, o = parts
                s, r, o = s.strip(), r.lower().strip(), o.strip()

                triplets.append((s, r, o))

                index[s.lower()].append((s, r, o))
                index[o.lower()].append((s, r, o))

                s_l, o_l = s.lower(), o.lower()

                if r in ("son of", "daughter of", "offspring of"):
                    parents_of[s_l].add(o_l)
                    children_of[o_l].add(s_l)

                elif r in ("mother of", "father of"):
                    parents_of[o_l].add(s_l)
                    children_of[s_l].add(o_l)

                elif r in ("husband of", "wife of", "married", "consort of"):
                    spouses_of[s_l].add(o_l)
                    spouses_of[o_l].add(s_l)

                elif r in ("brother of", "sister of", "half-brother of"):
                    siblings_of[s_l].add(o_l)
                    siblings_of[o_l].add(s_l)

                elif r == "charioteer of":
                    charioteer_map[s_l].add(o_l)

                elif r in ("enemy of", "fought", "slain by", "killed"):
                    enemies_of[s_l].add(o_l)

                else:
                    actions[s_l].append((r, o_l))

    # =========================
    # LOAD TTL
    # =========================
    ttl_graph = Graph()
    ttl_graph.parse(TTL_FILE, format="ttl")

    for subj, pred, obj in ttl_graph:
        s = str(subj).split("/")[-1].lower()
        r = str(pred).split("/")[-1].replace("_", " ").lower()
        o = str(obj).split("/")[-1].lower()

        index[s].append((s, r, o))
        index[o].append((s, r, o))

        if r == "parent of":
            parents_of[o].add(s)
            children_of[s].add(o)

        elif r == "spouse of":
            spouses_of[s].add(o)
            spouses_of[o].add(s)

        elif r == "sibling of":
            siblings_of[s].add(o)
            siblings_of[o].add(s)

        elif r == "enemy of":
            enemies_of[s].add(o)

        else:
            actions[s].append((r, o))