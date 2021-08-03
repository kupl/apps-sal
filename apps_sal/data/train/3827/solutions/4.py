from math import acos, asin, atan, degrees


def missing_angle(h, a, o):
    return round(degrees(
        atan(o / a) if not h else
        asin(o / h) if not a else
        acos(a / h)
    ))
