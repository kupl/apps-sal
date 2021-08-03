import math


def find_next_power(val, pow_):
    next_power_value = math.floor(1 + val ** (1 / pow_))
    return next_power_value ** pow_
