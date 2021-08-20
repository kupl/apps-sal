import math


def missing_angle(h, a, o):
    if h == 0:
        h = (a ** 2 + o ** 2) ** 0.5
    if a == 0:
        a = (h * 2 - o ** 2) ** 0.5
    if o == 0:
        o = (h ** 2 - a ** 2) ** 0.5
    return round(math.asin(o / h) * 180 / math.pi)
