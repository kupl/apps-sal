import math


def dating_range(age):
    return f'{math.floor(age / 2 + 7)}-{(age - 7) * 2}' if int(age) > 14 else f'{int(age - 0.1 * age)}-{int(age + 0.1 * age)}'
