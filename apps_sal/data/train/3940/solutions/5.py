def find_children(santas, children):
    return sorted(set(children) & set(santas))
