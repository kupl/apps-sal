import math


def tankvol(h, d, vt):
    r = d / 2
    theta = math.acos((r - h) / r)
    return int(vt * (theta - math.sin(theta) * (r - h) / r) / math.pi)
