from math import log


def powerof4(n):
    return n == 4 ** round(log(n, 4)) if type(n) == int and n > 0 else False
