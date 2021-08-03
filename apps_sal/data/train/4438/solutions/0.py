def middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    return sorted(((x1, y1, z1, 1), (x2, y2, z2, 2), (x3, y3, z3, 3)))[1][3]
