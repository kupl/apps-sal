def symmetric_point(p, q):
    xpos = p[0] < q[0]
    ypos = p[1] < q[1]
    xdiff = max(p[0], q[0]) - min(p[0], q[0])
    ydiff = max(p[1], q[1]) - min(p[1], q[1])
    if xpos:
        x = q[0] + xdiff
    if not xpos:
        x = q[0] - xdiff
    if ypos:
        y = q[1] + ydiff
    if not ypos:
        y = q[1] - ydiff
    return [x, y]
