import random

CERTAINTY = 10  # False positive rate: 4 ** -CERTAINTY


def number_property(n):
    return [is_prime(n), n % 2 == 0, n % 10 == 0]


def is_prime(n, k=CERTAINTY):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    s, d = _factorize(n - 1)

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if _is_witness(x, n, s):
            return False

    return True  # Probably


def _factorize(n):
    i = 0
    while n % 2 == 0:
        n >>= 1
        i += 1
    return i, n


def _is_witness(x, n, s):
    if x == 1 or x == n - 1:
        return False

    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == 1:
            return True
        if x == n - 1:
            return False

    return True
