def symmetric_point(p, q):
    xnew = q[0] + (q[0] - p[0])
    ynew = q[1] + (q[1] - p[1])
    return [xnew, ynew]
