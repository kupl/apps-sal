from math import copysign as sign


def reverse_invert(lst):
    return [-int(sign(int(str(abs(x))[::-1]), x)) for x in lst if isinstance(x, int)]
