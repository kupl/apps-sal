import math


def solve(n):
    for i in range(math.ceil(n ** 0.5) - 1, 0, -1):
        if n % i == 0:
            bma = n / i - i
            if bma % 2 == 0:
                return (bma / 2) ** 2
    return -1
