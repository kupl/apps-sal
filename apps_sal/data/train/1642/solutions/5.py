from collections import Counter
from functools import reduce
from operator import mul


small_primes = [2]


def is_prime(n):
    for p in small_primes:
        if p * p > n:
            return True
        if n % p == 0:
            return False


for n in range(3, 1000000):
    if is_prime(n):
        small_primes.append(n)


def factor(n):
    if n == 1:
        return Counter()
    for p in small_primes:
        if n % p != 0:
            continue
        factors = factor(n // p)
        factors[p] += 1
        return factors
    return Counter({n: 1})


def count_partitions(k, r):
    numerator = reduce(mul, list(range(r + 1, r + k)), 1)
    denominator = reduce(mul, list(range(1, k)), 1)
    return numerator // denominator


def multiply(n, k):
    factors = factor(n)
    print(n)
    print(factors)
    return reduce(mul, [count_partitions(k, r) for r in list(factors.values())], 1)
