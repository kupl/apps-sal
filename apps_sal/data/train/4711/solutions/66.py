import math


def zeros(n):
    ret = 0
    if n == 0:
        return 0
    for i in range(1, int(math.log(n) / math.log(5)) + 1):
        ret += n // math.pow(5, i)
    return ret
