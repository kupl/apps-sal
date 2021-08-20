def symmetric_point(p, q):
    return [r + r - s for (s, r) in zip(p, q)]
