from math import log


def power_law(x1y1, x2y2, x3):
    try:
        k = (log(x1y1[1]) - log(x2y2[1])) / (log(x1y1[0]) - log(x2y2[0]))
        a = x1y1[1] / (x1y1[0] ** k)
        return round(a * x3 ** k)
    except ZeroDivisionError:
        return x2y2[1]
