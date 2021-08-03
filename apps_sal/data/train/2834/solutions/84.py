def symmetric_point(p, q):
    p2_x = p[0] + 2 * (q[0] - p[0])
    p2_y = p[1] + 2 * (q[1] - p[1])
    return [p2_x, p2_y]
