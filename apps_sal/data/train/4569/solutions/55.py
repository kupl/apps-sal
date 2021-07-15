def next_item(xs, item):
    return_next = False
    for elem in xs:
        if return_next:
            return elem
        elif elem == item:
            return_next = True
    return None
