def symmetric_point(p, q):
    if p[0] > q[0]:
        x0 = q[0] - (p[0] - q[0])
        if p[1] > q[1]:
            y0 = q[1] - (p[1] - q[1])
            return [x0, y0]
        else:
            y0 = q[1] - (p[1] - q[1])
            return [x0, y0]
    else:
        x0 = q[0] - (p[0] - q[0])
        if p[1] > q[1]:
            y0 = q[1] - (p[1] - q[1])
            return [x0, y0]
        else:
            y0 = q[1] - (p[1] - q[1])
            return [x0, y0]
