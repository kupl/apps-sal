from math import floor


def find(n):
    return sum(3 * i for i in range(1, floor(n / 3) + 1)) + sum(5 * i for i in range(1, floor(n / 5) + 1) if (5 * i) % 3 != 0)
