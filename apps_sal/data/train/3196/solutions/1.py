from math import ceil


def root(n): return ((1 + 8 * n)**.5 - 1) / 2


def triangular_range(s, e):
    return {i: -~i * i >> 1 for i in range(ceil(root(s)), int(root(e)) + 1)}
