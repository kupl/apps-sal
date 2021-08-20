from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all((n % i for i in islice(count(2), int(sqrt(n) - 1))))


def gap(g, m, n):
    last_prime = None
    for i in range(m, n + 1):
        if isPrime(i):
            if last_prime is not None:
                if i - last_prime == g:
                    return [last_prime, i]
            last_prime = i
    return None
