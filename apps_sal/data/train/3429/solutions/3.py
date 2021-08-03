from numbers import Number
import math


def circleArea(r):
    if isinstance(r, Number):
        if r > 0:
            return round(r * r * math.pi, 2)
        else:
            return False
    else:
        return False
