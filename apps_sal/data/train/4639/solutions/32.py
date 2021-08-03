import math


def power_of_two(x):
    return x == 2**(int(math.log(x, 2))) if x > 0 else False
