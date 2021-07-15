def find_children(santas_list, children):
    return sorted([names for names in santas_list if names in children])
