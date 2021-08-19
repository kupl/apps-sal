def symmetric_point(p, q):
    return [b + (b - a) for (a, b) in zip(p, q)]
