
from math import sin, acos, pi


def tankvol(h, d, vt):
    r = d / 2.0
    theta = 2 * acos(1 - h / r)
    A_segment = r**2 / 2 * (theta - sin(theta))
    A_circle = r**2 * pi
    ratio = A_segment / A_circle
    vol_remain = ratio * vt
    return int(vol_remain)
