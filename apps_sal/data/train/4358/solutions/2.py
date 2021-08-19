import math


def ellipse_contains_point(f0, f1, l, p):

    def calc_len(f):
        return math.hypot(*(f[a] - p[a] for a in 'xy'))
    return calc_len(f0) + calc_len(f1) <= l
