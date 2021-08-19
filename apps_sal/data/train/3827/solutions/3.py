from math import sqrt, asin, degrees


def missing_angle(h, a, o):
    (h, o) = (h or sqrt(a ** 2 + o ** 2), o or sqrt(h ** 2 - a ** 2))
    return round(degrees(asin(o / h)))
