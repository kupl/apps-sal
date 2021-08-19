from math import ceil


def count_number(n, x):
    return sum((x % a == 0 for a in range(ceil(x / n), n + 1)))
