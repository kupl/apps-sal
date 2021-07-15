from math import hypot

def coordinates(p1, p2, precision=0):
    return round(hypot(p1[0] - p2[0], p1[1] - p2[1]), precision)
