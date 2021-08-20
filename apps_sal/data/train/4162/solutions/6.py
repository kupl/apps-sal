from math import log, ceil


def friends(n):
    return 0 if n < 2 else ceil(log(n, 2) - 1)
