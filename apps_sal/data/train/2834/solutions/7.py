def symmetric_point(p, q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    return [q[0]+dx, q[1]+dy]
