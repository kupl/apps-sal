from math import log2
def power_of_two(x):
    if x <= 0:
        return False
    return x == 2**int(log2(x))
