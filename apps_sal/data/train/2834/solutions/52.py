def symmetric_point(p, q):
    [a, b] = p
    [c, d] = q
    p = c - a
    q = d - b
    return [c + p, d + q]
