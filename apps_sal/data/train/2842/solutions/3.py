from math import hypot


def coordinates(p1, p2, r=0):
    x1, y1 = p1
    x2, y2 = p2
    return round(hypot(x2 - x1, y2 - y1), r)
