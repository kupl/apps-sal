import math
def is_negative_zero(n):
    return n == 0 and math.copysign(1, n) == -1
