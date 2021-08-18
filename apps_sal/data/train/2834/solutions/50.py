def symmetric_point(p, q):
    a = [0, 0]
    a[0] = q[0] - abs(p[0] - q[0]) if (p[0] > q[0]) else q[0] + abs(p[0] - q[0])
    a[1] = q[1] - abs(p[1] - q[1]) if p[1] > q[1] else q[1] + abs(p[1] - q[1])
    return a
