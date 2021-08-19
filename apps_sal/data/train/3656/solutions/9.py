from fractions import Fraction
from math import ceil


def decompose(n):
    n = Fraction(n)
    (lst, n) = ([int(n)], n - int(n))
    while n > 0:
        next_denom = int(ceil(1 / n))
        lst.append(next_denom)
        n -= Fraction(1, next_denom)
    return ([] if lst[0] == 0 else [str(lst[0])]) + ['1/{}'.format(d) for d in lst[1:]]
