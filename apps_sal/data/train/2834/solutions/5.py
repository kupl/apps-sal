def symmetric_point(p, q):
    return [a * 2 - b for (a, b) in zip(q, p)]
