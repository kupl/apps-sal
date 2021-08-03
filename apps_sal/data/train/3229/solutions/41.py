import math


def am_i_wilson(n):

    if type(n) != int:
        return False

    if n == 0 or n == 1 or n == 2:
        return False

    for i in range(2, n):
        if (n % i) == 0:
            return False

    return (math.factorial((n - 1)) + 1) % (n * n) == 0
