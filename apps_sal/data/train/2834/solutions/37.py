def symmetric_point(p, q):
    x = q[0] - p[0]
    x = q[0] + x
    y = q[1] - p[1]
    y = q[1] + y
    return [x,y]

