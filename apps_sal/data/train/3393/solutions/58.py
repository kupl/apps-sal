import collections
import itertools
import numpy as np


def binary_check(x):
    if x == 1:
        return True
    start = 0
    stop = x // 2
    sol = []
    while start <= stop:
        mid = (start + stop) // 2

        if mid * mid == x:
            return True
        if mid * mid < x:
            start = mid + 1
        if mid * mid > x:
            stop = mid - 1


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in list(pf_with_multiplicity.items())
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


def list_squared(m, n):
    sol = []

    for number in range(m, n):
        candidate = [i**2 for i in range(1, number + 2) if number % i == 0]
        n = sum(candidate)
        if binary_check(n):
            sol.append([number, n])
    return sol


def list_squared(m, n):
    sol = []
    for number in range(m, n):
        candidate = [i * i for i in get_divisors(number)]
        n = int(sum(candidate))
        if binary_check(n):
            sol.append([number, n])
    return sol
