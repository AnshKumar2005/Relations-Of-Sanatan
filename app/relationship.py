from app.data_loader import parents_of, children_of, spouses_of


def extract_relationship(a, b):
    a, b = a.lower(), b.lower()

    if b in spouses_of[a]:
        return f"{a.capitalize()} is spouse of {b.capitalize()}."

    if b in parents_of[a]:
        return f"{a.capitalize()} is child of {b.capitalize()}."

    if b in children_of[a]:
        return f"{a.capitalize()} is parent of {b.capitalize()}."

    return "No direct relationship found."