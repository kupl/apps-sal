from math import ceil


def count_number(n, x):
    return sum((x % i == 0) and (x / i != i) + 1 for i in range(ceil(x / n), int(x**0.5) + 1))
