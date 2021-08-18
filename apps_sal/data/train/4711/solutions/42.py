import math


def zeros(n):
    sum = 0
    if n < 5:
        return 0
    for i in range(1, math.floor(math.log(n, 5) + 1)):
        sum += math.floor(n / pow(5, i))
    return sum
