import math


def series_sum(n):
    result = 0.0
    for i in list(range(0, n)):
        result += 1.0 / (1.0 + 3.0 * float(i))
    return '{:.2f}'.format(result)
