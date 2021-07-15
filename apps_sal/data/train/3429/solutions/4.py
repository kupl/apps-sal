from numbers import Number
import math
def circleArea(r):
    if (not isinstance(r, Number)) or (r < 0):
        return False
    return round(math.pi * r * r, 2)

