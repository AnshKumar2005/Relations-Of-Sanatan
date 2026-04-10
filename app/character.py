from app.data_loader import index


def describe_character(name):
    name = name.strip().lower()

    if not name:
        return "Please enter a mythological character name."

    if name not in index:
        return f"No information found for {name}."

    main = name.capitalize()
    facts = index[name]

    male_signals = {"son of", "husband of", "father of", "king of", "regent of"}
    female_signals = {"daughter of", "wife of", "mother of", "queen of"}

    gender = None
    for s, r, o in facts:
        if s.lower() == name:
            if r in male_signals:
                gender = "male"
                break
            if r in female_signals:
                gender = "female"

    pronoun = "He" if gender != "female" else "She"

    parents, spouses, children, aliases = [], [], [], []
    kingdoms, regencies, teachers = [], [], []
    battles, relations, roles = [], [], []

    for s, r, o in facts:
        if s.lower() != name:
            continue

        o_l = o.lower()

        if "type" in r or "class" in r:
            roles.append(o_l)

        elif r in ("son of", "daughter of"):
            parents.append(o_l)

        elif r in ("husband of", "wife of"):
            spouses.append(o_l)

        elif r in ("father of", "mother of"):
            children.append(o_l)

        elif r == "also known as":
            aliases.append(o_l)

        elif r in ("king of", "ruler of"):
            kingdoms.append(o_l)

        elif r == "regent of":
            regencies.append(o_l)

        elif r in ("student of", "trained by"):
            teachers.append(o_l)

        elif r in ("fought", "defeated", "killed"):
            battles.append(f"{r} {o_l}")

        else:
            relations.append(f"{r} {o_l}")

    def uniq(x): return sorted(set(x))

    sentences = []

    if roles:
        sentences.append(f"{main} is a {', '.join(uniq(roles))}.")
    if parents:
        sentences.append(f"{main} was born to {' and '.join(uniq(parents))}.")
    if spouses:
        sentences.append(f"{pronoun} was married to {', '.join(uniq(spouses))}.")

    return " ".join(sentences)