def symmetric_point(p, q):
    p1x = q[0] + (q[0] - p[0])
    p1y = q[1] + (q[1] - p[1])
    return [p1x, p1y]
