from math import factorial


def am_i_wilson(n):
    return True if n > 1 and n < 1000 and ((factorial(n - 1) + 1) % n ** 2 == 0) else False
