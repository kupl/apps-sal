from math import log


def power_of_two(x):
    return 2 ** int(log(x, 2)) == x if x else False
