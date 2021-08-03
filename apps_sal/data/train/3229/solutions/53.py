from math import sqrt, factorial


def am_i_wilson(n):
    return False if n <= 1 else is_prime(n) and (factorial(n - 1) + 1) % (n * n) == 0


def is_prime(n):
    return len([x for x in range(2, int(sqrt(n)) + 1) if n % x == 0]) == 0
