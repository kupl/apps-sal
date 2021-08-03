import numbers
import math
from fractions import Fraction


def primeFactors(n):
    c = n
    p = []
    while n % 2 == 0:
        if not 2 in p:
            p.append(2)
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if not i in p:
                p.append(int(i))
            n /= i
    if n != 1:
        p.append(int(n))
    return p or [c]


def totient(n):
    if not isinstance(n, numbers.Number) or n < 1:
        return 0
    if n == 1:
        return n
    res = Fraction(1, 1)
    print((n, primeFactors(n)))
    for p in primeFactors(n):
        res *= Fraction(p - 1, p)
    return Fraction(n, 1) * res
