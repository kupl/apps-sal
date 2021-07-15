from math import ceil

def find_next_power(val, pow_):
    return ceil((val + 1) ** (1 / pow_)) ** pow_
