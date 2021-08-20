from math import log


def power_law(x1y1, x2y2, x3):
    (x1, y1) = x1y1
    (x2, y2) = x2y2
    if x1 == x2 == x3:
        return y1
    k = -log(y2 / y1, x1 / x2)
    a = y1 / x1 ** k
    return round(a * x3 ** k)
