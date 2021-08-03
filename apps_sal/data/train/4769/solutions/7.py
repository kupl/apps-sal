import math


def area(d, l):

    if d < l or d == l:
        return ("Not a rectangle")

    if l == 0 and d == 0:
        return ("Not a rectangle")

    x = math.sqrt(d**2 - l**2)

    ar = round(x * l, 2)

    return ar
