from math import pi


def circleArea(r):
    return round(pi * r * r, 2) if type(r) != str and r > 0 else False
