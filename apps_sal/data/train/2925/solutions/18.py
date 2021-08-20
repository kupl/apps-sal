import math


def multiply(n):
    if n > 0:
        digits = int(math.log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n)) + 2
    if n > 0:
        return 5 ** digits * n
    else:
        return 5 ** (digits - 1) * n
