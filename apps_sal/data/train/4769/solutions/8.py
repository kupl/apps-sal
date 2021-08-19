import math


def area(d, l):
    if d <= l:
        return 'Not a rectangle'
    s2 = d ** 2 - l ** 2
    s = math.sqrt(s2)
    return round(l * s, 2)
