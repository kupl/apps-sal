from math import *
def power_of_two(x):
    return x == 2**ceil(log2(x)) if x > 0 else 0
