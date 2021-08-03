from functools import reduce


def billboard(n, p=30): return reduce(lambda a, b: a + p, n, 0)
