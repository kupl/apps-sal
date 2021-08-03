import math


def missing_angle(h, a, o):
    if h > 0 and a > 0:
        result = math.acos(a / h)
    elif a == 0 and o > 0:
        result = math.asin(o / h)
    elif h == 0 and o > 0:
        result = math.atan(o / a)
    else:
        raise ValueError("Invalid argument(s)")

    return round(math.degrees(result))
