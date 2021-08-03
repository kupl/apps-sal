def symmetric_point(p, q):
    dist_x = p[0] - q[0]
    dist_y = p[1] - q[1]
    return [q[0] - dist_x, q[1] - dist_y]
