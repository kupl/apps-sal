from math import log2
def power_of_two(x):
    if x<1:
        return False
    return 2**int(log2(x)) == x
