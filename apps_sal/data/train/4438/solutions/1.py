def middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    return max(((x2 - x3) ** 2 + (y2 - y3) ** 2 + (z2 - z3) ** 2, 1), ((x1 - x3) ** 2 + (y1 - y3) ** 2 + (z1 - z3) ** 2, 2), ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2, 3))[1]
