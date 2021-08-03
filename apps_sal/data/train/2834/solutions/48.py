def symmetric_point(p, q):
    return [abs(p[i] - q[i]) + q[i] if p[i] < q[i] else q[i] - abs(p[i] - q[i]) for i in [0, 1]]
