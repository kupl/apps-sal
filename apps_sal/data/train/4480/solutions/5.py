def parse(data):
    (v, r) = (0, [])
    for c in data:
        (v, r) = (v + {'i': 1, 'd': -1, 's': v * (v - 1)}.get(c, 0), r + [v] * (c == 'o'))
    return r
