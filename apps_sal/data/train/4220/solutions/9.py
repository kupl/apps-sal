from math import sqrt


def equable_triangle(a, b, c):
    perimeter = a + b + c
    ss = perimeter / 2
    try:
        area = sqrt(ss * (ss - a) * (ss - b) * (ss - c))
    except ValueError:
        return False
    return area == perimeter
