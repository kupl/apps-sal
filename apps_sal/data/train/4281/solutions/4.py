from math import pi, acos, sin


def tankvol(h, d, vt):
    theta = acos((d - 2 * h) / d)
    proportion = (theta - 0.5 * sin(2 * theta)) / pi
    return int(proportion * vt)
