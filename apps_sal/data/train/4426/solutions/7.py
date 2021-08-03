import math


def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


def isMultiple(a, b, n):
    to_test = normal_round((a / b - int(a / b)) * 10)
    if to_test >= 10:
        return False
    else:
        return to_test > 0 and to_test % n == 0
