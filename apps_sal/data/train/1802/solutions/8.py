from math import gcd
from functools import reduce


def frobenius_number(a):

    def __residue_table(a):
        n = [0] + [None] * (a[0] - 1)
        for i in range(1, len(a)):
            d = gcd(a[0], a[i])
            for r in range(d):
                try:
                    nn = min((n[q] for q in range(r, a[0], d) if n[q] is not None))
                except ValueError:
                    continue
                if nn is not None:
                    for c in range(a[0] // d):
                        nn += a[i]
                        p = nn % a[0]
                        nn = min(nn, n[p]) if n[p] is not None else nn
                        n[p] = nn
        return n
    if len(a) < 2 or reduce(gcd, a) > 1:
        return -1
    return max(__residue_table(sorted(a))) - min(a)


def min_price(coins):
    if min(coins) == 1:
        return 1
    f = frobenius_number(coins)
    return f + 1 if f >= 0 else -1
