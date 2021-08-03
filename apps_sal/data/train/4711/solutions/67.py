import math


def zeros(n):
    if n == 0:
        return 0
    z = 0
    kmax = math.floor(math.log(n) / math.log(5))
    for i in range(1, kmax + 1):
        z += math.floor(n / 5**i)

    return z
