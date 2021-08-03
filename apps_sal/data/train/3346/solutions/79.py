import math


def is_prime(i):
    if i == 2:
        return True
    for x in range(2, math.ceil(math.sqrt(i)) + 1):
        if i % x == 0:
            return False
    return True


def gap(g, m, n):
    primes = []
    for i in range(m, n + 1):
        if is_prime(i):
            if len(primes) > 0 and primes[-1] == i - g:
                print([i - g, i])
                return [i - g, i]
            primes.append(i)
