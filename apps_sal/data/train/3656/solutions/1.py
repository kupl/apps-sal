from fractions import Fraction
from math import ceil


def decompose(n):
    try:
        n = Fraction(n)
    except ValueError:
        return []
    try:
        e = int(n)
    except ValueError:
        return []
    if n == 0:
        return []
    if n == e:
        return [str(n)]
    n -= e
    if e != 0:
        l = [str(e)]
    else:
        l = []
    while n.numerator > 1:
        e = Fraction(1, int(ceil(1 / n)))
        l.append(str(e.numerator) + '/' + str(e.denominator))
        n -= e
    l.append(str(n.numerator) + '/' + str(n.denominator))
    return l
