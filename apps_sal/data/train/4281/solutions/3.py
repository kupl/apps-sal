# see https://en.wikipedia.org/wiki/Circular_segment
# for the formulas used

from math import sin, acos, pi


def tankvol(h, d, vt):
    # radius
    r = d / 2.0
    # central angle of segment
    theta = 2 * acos(1 - h / r)
    # area of segment
    A_segment = r**2 / 2 * (theta - sin(theta))
    # area of circle
    A_circle = r**2 * pi
    # ratio of the areas
    ratio = A_segment / A_circle
    # remaining volume
    vol_remain = ratio * vt
    # return the truncated result
    return int(vol_remain)
