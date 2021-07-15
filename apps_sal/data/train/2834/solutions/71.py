def symmetric_point(p, q):
    c = int(q[0] + (q[0] - p[0]))   
    d = int(q[1] + (q[1] - p[1]))
    return [c, d]
