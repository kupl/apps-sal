def symmetric_point(p, q):
    distance = (q[0] - p[0], q[1] - p[1])
    symetric = [q[0] + distance[0], q[1] + distance[1]]
    return symetric
