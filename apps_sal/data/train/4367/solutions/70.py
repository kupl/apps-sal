from math import *


def area_or_perimeter(l, w):
    if l == w:
        area = l * w
        return area
    else:
        p = l + w + l + w
        return p
