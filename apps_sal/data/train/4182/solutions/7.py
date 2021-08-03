import math


def survivor(n):
    for i in range(2, n):
        if n < i:
            break
        if n % i == 0:
            return False
        n = n - n // i
    return True
