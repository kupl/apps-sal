from math import log


def powerof4(n):
    return type(n) == int and n >= 0 and log(n, 4).is_integer()
