from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def odd_not_prime(n):
    return sum((not isPrime(i)) & (i % 2 != 0)for i in range(1, n + 1))
