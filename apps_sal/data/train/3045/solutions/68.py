import math


def elevator(left, right, call):
    diff1 = abs(left - call)
    diff2 = abs(right - call)
    if diff1 < diff2:
        return 'left'
    elif diff2 > diff1:
        return 'right'
    else:
        return 'right'
