def middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    import math

    def dist(x1, y1, z1, x2, y2, z2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    if math.fabs(dist(x1, y1, z1, x2, y2, z2) + dist(x1, y1, z1, x3, y3, z3) - dist(x2, y2, z2, x3, y3, z3)) < 0.1:
        return 1
    if math.fabs(dist(x2, y2, z2, x1, y1, z1) + dist(x2, y2, z2, x3, y3, z3) - dist(x1, y1, z1, x3, y3, z3)) < 0.1:
        return 2
    return 3
