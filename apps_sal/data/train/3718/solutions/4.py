from math import sqrt, floor


def divisors(n):
    return sum(1 if i * i == n else 2 for i in range(1, floor(sqrt(n) + 1)) if n % i == 0)
