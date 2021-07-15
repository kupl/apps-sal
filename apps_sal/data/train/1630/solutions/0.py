from functools import reduce
from math import gcd

def survivor(a):
    """Round Robin by Bocker & Liptak"""
    def __residue_table(a):
        n = [0] + [None] * (a[0] - 1)
        for i in range(1, len(a)):
            d = gcd(a[0], a[i])
            for r in range(d):
                try:
                    nn = min(n[q] for q in range(r, a[0], d) if n[q] is not None)
                except ValueError:
                    continue
                for _ in range(a[0] // d):
                    nn += a[i]
                    p = nn % a[0]
                    if n[p] is not None: nn = min(nn, n[p])
                    n[p] = nn
        return n

    a.sort()
    if len(a) < 1 or reduce(gcd, a) > 1: return -1
    if a[0] == 1: return 0
    return max(__residue_table(a)) - a[0]
