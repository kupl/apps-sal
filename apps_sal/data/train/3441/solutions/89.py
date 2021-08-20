import math


def get_average(marks):
    res = 0
    for i in marks:
        res = i + res
    return math.floor(res / len(marks))
    raise NotImplementedError('TODO: get_average')
