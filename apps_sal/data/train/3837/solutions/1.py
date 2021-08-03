from functools import reduce


def reverse(r):
    return reduce(lambda a, n: reduce(lambda b, s: b.append(s - b[-1]) or b, reversed(a), [n])[::-1], r, [])
