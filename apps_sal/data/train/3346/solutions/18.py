import math


def gap(g, a, b):
    primes = []
    for n in range(a, b):
        if all((n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))):
            if primes != [] and n - primes[-1] == g:
                return [primes[-1], n]
            primes.append(n)
    return None
