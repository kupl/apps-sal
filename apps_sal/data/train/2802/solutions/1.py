from functools import reduce


def per(n):
    r = []
    p = reduce(lambda a, b: a * b, map(int, str(n)))
    return r if p == n else [p] + per(p)
