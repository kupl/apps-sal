import math


def zeros(n):
    if n == 0:
        return 0
    fives = 0
    log5n = int(math.log10(n) / math.log10(5))
    for i in range(1, log5n + 1):
        fives += int(n / 5 ** i)
    return int(fives)
