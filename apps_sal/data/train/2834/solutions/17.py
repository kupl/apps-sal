def symmetric_point(p, q):
    return list(map(lambda a, b: a + b, q, list(map(lambda a, b: b - a, p, q))))

