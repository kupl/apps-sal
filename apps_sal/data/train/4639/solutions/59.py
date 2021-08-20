import math


def power_of_two(x):
    exp_val = int(math.log(x) / math.log(2)) if x else 0
    return True if x > 0 and 2 ** exp_val == x else False
