import math


def close_compare(a, b, margin=0):
    if math.fabs(a - b) <= margin:
        return 0
    if a < b:
        return -1
    return 1
