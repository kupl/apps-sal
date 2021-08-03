from functools import reduce
M = 10**9 + 7


def solve(s):
    return reduce(lambda p, n: ((p[0] * 26 + (90 - n)) % M, ((p[0] + 1) * (90 - n) + p[1]) % M), map(ord, s), (0, 0))[1]
