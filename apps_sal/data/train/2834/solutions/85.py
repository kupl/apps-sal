def symmetric_point(p, q):
    a = q[0] - p[0]
    b = q[1] - p[1]
    c = a + q[0]
    d = b + q[1]
    return [c, d]
