def sort_string(s, ordering):
    order = {}
    for (i, c) in enumerate(ordering):
        if c in order:
            continue
        order[c] = i
    return ''.join(sorted(s, key=lambda c: order.get(c, 9999)))
