from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all((n % i for i in islice(count(2), int(sqrt(n) - 1))))


def gap(g, m, n):
    prime = 0 - g
    for i in range(m, n):
        if is_prime(i):
            if i - prime == g:
                return [prime, i]
            prime = i
    else:
        return None
