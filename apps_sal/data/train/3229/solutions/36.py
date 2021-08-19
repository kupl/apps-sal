import math


def am_i_wilson(n):
    if n < 2 or n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return (math.factorial(n - 1) + 1) % n ** 2 == 0
