from fractions import Fraction
from collections import Counter


def isPrime(n):
    if n < 3 or not n % 2:
        return n == 2
    return all((n % x for x in range(3, int(n ** 0.5) + 1, 2)))


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n


def rec(current, k):
    if not k:
        return []
    if current == 1:
        return [1] * k
    return [current] + rec(current * sum((Fraction(v, k) for (k, v) in Counter(prime_factors(current)).items())), k - 1)


def chain_arith_deriv(start, k):
    if isPrime(start):
        return '{} is a prime number'.format(start)
    return rec(start, k)
