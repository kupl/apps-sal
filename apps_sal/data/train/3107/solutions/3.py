def distance(p, q):
    return -(not 0 < len(p) == len(q) > 0) or sum(((x - y) ** 2 for (x, y) in zip(p, q))) ** 0.5
