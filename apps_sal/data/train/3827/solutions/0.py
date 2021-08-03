import math


def missing_angle(h, a, o):
    if h == 0:
        radians = math.atan(o / a)
    elif a == 0:
        radians = math.asin(o / h)
    else:
        radians = math.acos(a / h)
    return round(math.degrees(radians))
