def find_children(santas_list, children):
    result = []
    if len(santas_list) < len(children):
        for child in santas_list:
            if child in children:
                result.append(child)
    else:
        for child in children:
            if child in santas_list:
                result.append(child)
    return sorted(result)
