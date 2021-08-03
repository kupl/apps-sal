def symmetric_point(p, q):
    x = [0, 0]

    x[0] = 2 * q[0] - p[0]
    x[1] = 2 * q[1] - p[1]

    return x
