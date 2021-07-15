def symmetric_point(p, q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    nx = dx + q[0]
    ny = dy + q[1]
    return [nx, ny]
