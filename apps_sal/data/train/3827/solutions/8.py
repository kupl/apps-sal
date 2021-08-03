import math


def missing_angle(h, a, o):
    if not h:
        h = (a**2 + o**2)**0.5
    if not o:
        o = (h**2 - a**2)**0.5
    return round(math.asin(o / h) * 180 / math.pi)
