from math import log


def zeros(n):
    if(n == 0):
        return 0
    return sum([int(n / 5**i) for i in range(1, int(log(n, 5)) + 1)])
