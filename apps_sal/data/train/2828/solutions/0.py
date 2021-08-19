from math import log


def power_law(p1, p2, x3):
    ((x1, y1), (x2, y2)) = (p1, p2)
    x1 += 1e-09
    y1 += 1e-09
    return round(y1 * (y2 / y1) ** log(x3 / x1, x2 / x1))
