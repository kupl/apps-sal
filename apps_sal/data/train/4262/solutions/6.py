from math import floor


def calc_tip(p, r):
    t = floor(0.1 * p + 0.5)
    return max(0, {1: t + 1, 0: t - 1, -1: t // 2 - 1}[r])
