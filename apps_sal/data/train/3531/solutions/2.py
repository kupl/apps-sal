def valid_mersenne(n):
    return n == 2 or (is_prime(n) and lucas_lehmer(n))


def is_prime(n):
    from itertools import chain
    return all((n % i != 0 for i in chain([2], range(3, int(n ** 0.5) + 1, 2))))


def lucas_lehmer(n):
    s = 4
    M = 2 ** n - 1
    for _ in range(n - 2):
        s = (s * s - 2) % M
    return s == 0
