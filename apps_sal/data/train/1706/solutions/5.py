from math import sqrt


def rectangle_rotation(a, b):
    d = sqrt(2)
    x1 = int(a / (2 * d)) * 2 + 1
    y1 = int(b / (2 * d)) * 2 + 1
    x2 = 2 * (1 + int(a / (2 * d) - 1 / 2))
    y2 = 2 * (1 + int(b / (2 * d) - 1 / 2))
    return x1 * y1 + x2 * y2
