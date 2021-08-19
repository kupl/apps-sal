import math


def tankvol(h, d, vt):
    r = d / 2.0
    if h == r:
        return vt / 2
    half = h > r
    h = d - h if half else h
    a = r - h
    b = math.sqrt(r ** 2 - a ** 2)
    t = 2 * math.asin(b / r)
    A = r ** 2 * t / 2 - b * a
    v = vt * A / (math.pi * r ** 2)
    return int(vt - v) if half else int(v)
