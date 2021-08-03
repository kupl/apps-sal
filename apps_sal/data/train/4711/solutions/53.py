import math


def zeros(n):
    if n <= 0:
        return 0
    k_max = math.floor(math.log(n, 5)) + 1
    sum = 0
    for k in range(1, k_max):
        sum += math.floor(n / 5 ** k)
    return sum
