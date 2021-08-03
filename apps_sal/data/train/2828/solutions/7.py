from math import log


def power_law(x1y1, x2y2, x3):
    (x1, y1), (x2, y2) = (x1y1, x2y2)
    try:
        k = log(y1 / y2, x1 / x2)
        a = y1 / x1 ** k
        return round(a * x3 ** k)
    except ZeroDivisionError:
        return y2
