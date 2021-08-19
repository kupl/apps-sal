def symmetric_point(p, q):
    return [y + (y - x) for (x, y) in zip(p, q)]
