from math import log


def power_of_two(x):
    return (x > 0) and 2**int(log(x, 2)) == x
