from fractions import gcd
from functools import reduce


def DPC_sequence(s):
    ds, ps, cs, prod = [], [], [], 1

    for i, v in enumerate(s, 1):
        if v == 'D':
            ds.append(i)
            prod = (prod * i) // gcd(prod, i)
        elif v == 'P':
            ps.append(i)
        elif v == 'C':
            cs.append(i)

    for p in ps:
        if gcd(prod, p) != 1:
            return -1
    for c in cs:
        if prod % c == 0 or gcd(prod, c) == 1:
            return -1

    return prod
