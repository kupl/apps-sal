import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def gap(g, m, n):
    for i in range(m, n - g):
        r = list(range(i, i + g + 1))
        if is_prime(r[0]) and is_prime(r[-1]):
            if any((is_prime(n) for n in r[1:-1])):
                continue
            else:
                return [r[0], r[-1]]
