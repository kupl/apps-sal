def find_children(santas_list, children):
    return sorted(set(santas_list) & set(children))
