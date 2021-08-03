from math import log


def power_law(x1y1, x2y2, x3):
    x1, y1 = x1y1
    x2, y2 = x2y2
    if x1 == x2:
        return y2
    return round(y1 * (y2 / y1) ** log(x3 / x1, x2 / x1))
