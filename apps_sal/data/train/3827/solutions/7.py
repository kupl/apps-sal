from math import atan, asin, acos, pi


def missing_angle(h, a, o):
    return round(atan(o / a) * 180 / pi) if not h else round(asin(o / h) * 180 / pi) if not a else round(acos(a / h) * 180 / pi)
