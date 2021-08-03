from math import sqrt, floor
from math import floor, sqrt


def rectangle_rotation(a, b):

    sa = krissx(a)
    sb = krissx(b)
    ena = krisenx(sa)
    enb = krisenx(sb)
    p = krisif(sa)
    m = krisif(sb)

    return (ena * enb) + (ena + p) * (enb + m)


def krissx(x):
    f = sqrt(2)
    return x / f


def krisenx(sx):
    enx = sx // 2 * 2 + 1
    return enx


def krisif(sx):
    sxif = sx - sx // 2 * 2
    if sxif >= 1:
        return 1
    else:
        return -1
