import math


def circleArea(r):
    return type(r) in (int, float) and r > 0 and round(math.pi * r**2, 2)
