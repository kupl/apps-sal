from math import log


def compare_powers(*numbers):
    a, b = map(lambda n: n[1] * log(n[0]), numbers)
    return (a < b) - (a > b)
