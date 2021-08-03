import math


def count(n):
    if n is 0:
        return 0
    x = int(math.log(n, 2))
    return x * 2 ** (x - 1) + n - 2 ** x + 1 + count(n - 2 ** x)


def countOnes(left, right):
    return count(right) - count(left - 1)
