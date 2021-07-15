def symmetric_point(p, q):
    if q[0] > p[0]:
        x = q[0] + abs(q[0] - p[0])
    elif q[0] < p[0]:
        x = q[0] - abs(p[0] - q[0])
    else:
        x = p[0]
    if q[1] > p[1]:
        y = q[1] + abs(q[1] - p[1])
    elif q[1] < p[1]:
        y = q[1] - abs(p[1] - q[1])
    else:
        y = p[1]   
    return [x, y]
