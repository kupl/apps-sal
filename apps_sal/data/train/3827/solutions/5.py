from math import asin, acos, atan, pi


def missing_angle(h, a, o):
    ans = acos(a / h) if h * a else atan(o / a) if a * o else asin(o / h)
    return round(ans * 180 / pi)
