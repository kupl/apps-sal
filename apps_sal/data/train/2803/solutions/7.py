from math import gcd
from copy import copy


def DPC_sequence(s):
    d = [x for x, y in enumerate(s, 1) if y == 'D']
    p = [x for x, y in enumerate(s, 1) if y == 'P']
    c = [x for x, y in enumerate(s, 1) if y == 'C']
    D = lcm(d) if len(d) > 1 else d[0]
    return D if all(gcd(D, i) == 1 for i in p if i != 1) and all(1 < gcd(D, i) < i for i in c) else -1


def lcm(n):
    x = n.copy()
    while x:
        i, n = x[-2:]
        del x[-2:]
        if not x: return n
        x.append(i * n // gcd(i, n))
