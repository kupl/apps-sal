from math import acos, pi, sin, sqrt


def tankvol(h, d, vt):
    r = d / 2
    l = vt / (pi * r ** 2)
    v = l * (r ** 2 * acos((r - h) / r) - (r - h) * sqrt(2 * r * h - h ** 2))
    return int(v)
