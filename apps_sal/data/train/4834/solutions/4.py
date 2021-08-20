from math import sqrt
from itertools import count, islice


def isPrime(n):
    return n > 1 and all((n % i for i in islice(count(2), int(sqrt(n) - 1))))


def backwardsPrime(a, b):
    return [x for x in range(a, b + 1) if isPrime(x) and x > 10 and isPrime(int(str(x)[::-1])) and (int(str(x)[::-1]) != x)]
