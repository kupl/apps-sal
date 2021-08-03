from math import pi


def sort_by_area(a):
    return sorted(a, key=lambda x: x**2 * pi if isinstance(x, (int, float)) else x[0] * x[1])
