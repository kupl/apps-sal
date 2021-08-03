from math import log2


def half_life(ini, rem, t):
    return t / log2(ini / rem)
