def symmetric_point(p, q):
    vertical_d = q[1] - p[1]
    horiz_d = q[0] - p[0]
    vertical_d = vertical_d * -1
    horiz_d = horiz_d * -1
    x = q[0] - horiz_d
    y = q[1] - vertical_d
    return [x, y]
