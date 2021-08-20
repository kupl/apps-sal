from math import sqrt, ceil


def branch(n):
    if n == 1:
        return 0
    x = ceil(sqrt(n)) // 2 * 2
    return (n - 1 - (x - 1) ** 2) // x
