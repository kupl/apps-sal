from math import hypot


def length_of_line(array):
    ((a, b), (c, d)) = array
    return f'{hypot(a - c, b - d):.2f}'
