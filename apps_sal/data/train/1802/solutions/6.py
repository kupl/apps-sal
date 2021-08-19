# All credit to PuzzlingInPython's blog post on the Bocker Liptak algorithm for calculating the Frobenius number.

from math import gcd as builtin_gcd


def gcd(a, *r):
    for b in r:
        a = builtin_gcd(a, b)
    return a


def lcm(a, *r):
    for b in r:
        a *= b // builtin_gcd(a, b)
    return abs(a)


def frobenius_number(a):
    def __residue_table(a):
        n = [0] + [None] * (a[0] - 1)
        for i in range(1, len(a)):
            d = gcd(a[0], a[i])
            for r in range(d):
                try:
                    nn = min(n[q] for q in range(r, a[0], d) if n[q] is not None)
                except ValueError:
                    continue
                if nn is not None:
                    for c in range(a[0] // d):
                        nn += a[i]
                        p = nn % a[0]
                        nn = min(nn, n[p]) if n[p] is not None else nn
                        n[p] = nn
        return n

    if len(a) < 2 or gcd(*a) > 1:
        return -1
    return max(max(__residue_table(sorted(a))) - min(a) + 1, 1)


def min_price(coins):
    return frobenius_number(coins)
