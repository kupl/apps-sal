import math


def power_of_two(x):
    if x < 1:
        return False
    if x == 2 or x == 1:
        return True
    if x and (not x & x - 1):
        return True
    else:
        return False
