from math import log


def powerof4(n):
    return False if type(n) != int else int(log(n, 4)) == log(n, 4) if n > 0 else False
