def symmetric_point(p, q):
    p_1 = []
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    p_1.append(q[0] - dx)
    p_1.append(q[1] - dy)
    return p_1
