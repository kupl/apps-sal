import math


def power_of_two(x):
    if x == 0:
        return False
    else:
        return not x & x - 1
