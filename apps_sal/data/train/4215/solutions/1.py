from math import ceil


def count_number(n, x):
    return sum(x % i == 0 for i in range(max(int(ceil(x / n)), 1), min(n, x) + 1))
