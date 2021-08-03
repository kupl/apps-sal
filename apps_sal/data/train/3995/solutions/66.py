import math


def dating_range(age):
    if age <= 14:
        return f'{math.floor(age - 0.10 * age)}-{math.floor(age + 0.10 * age)}'
    return f'{age // 2 + 7}-{(age - 7) * 2}'
