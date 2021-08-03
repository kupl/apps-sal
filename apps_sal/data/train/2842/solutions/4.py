import math


def coordinates(p1, p2, p=0):
    return round(math.hypot(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])), p)
