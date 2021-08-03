from collections import defaultdict
from functools import reduce


def factorsOf(n):
    p, d = 2, defaultdict(int)
    while p * p <= n:
        while not n % p:
            d[p] += 1
            n //= p
        p += 2 - (p == 2)
    if n > 1:
        d[n] += 1
    return d


def mul_power(n, k):
    return reduce(int.__mul__, (f**((k - n) % k) for f, n in factorsOf(n).items()), 1)
