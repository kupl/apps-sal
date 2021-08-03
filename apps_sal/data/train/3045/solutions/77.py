from math import fabs


def elevator(left, right, call):
    return 'left' if fabs(call - left) < fabs(call - right) else 'right'
