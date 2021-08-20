from itertools import count, chain
from fractions import Fraction
from functools import reduce
from operator import mul


def primes(n):
    for x in chain([2], count(3, 2)):
        if n == 1:
            return
        if x ** 2 > n:
            yield Fraction(n - 1, n)
            return
        elif not n % x:
            yield Fraction(x - 1, x)
            while not n % x:
                n //= x


def totient(n):
    return reduce(mul, primes(n), n) if type(n) == int and n >= 1 else 0
