from math import factorial


def am_i_wilson(n):
    if n < 20000000000000:
        return n in (5, 13, 563)
    return ((factorial(n - 1) + 1) / (n ** 2)).is_integer()

