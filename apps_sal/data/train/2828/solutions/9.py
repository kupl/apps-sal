import math


def power_law(x1y1, x2y2, x3):
    x1 = x1y1[0]
    y1 = x1y1[1]
    x2 = x2y2[0]
    y2 = x2y2[1]
    x = x2 / x1
    y = y2 / y1
    if x1 == x2:
        return y2
    return round(y1 * y ** (math.log(x3 / x1) / math.log(x)))
