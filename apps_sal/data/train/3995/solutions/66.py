import math


def dating_range(age):
    if age <= 14:
        return f'{math.floor(age - 0.1 * age)}-{math.floor(age + 0.1 * age)}'
    return f'{age // 2 + 7}-{(age - 7) * 2}'
