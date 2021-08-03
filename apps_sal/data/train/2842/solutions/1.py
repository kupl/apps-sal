import math


def coordinates(p1, p2, precision=0):
    return round(math.hypot(p1[0] - p2[0], p1[1] - p2[1]), precision)
