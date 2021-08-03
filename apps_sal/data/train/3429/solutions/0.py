from math import pi


def circleArea(r):
    return round(pi * r ** 2, 2) if type(r) in (int, float) and r > 0 else False
