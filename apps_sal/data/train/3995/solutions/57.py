import math


def dating_range(age):
    if age <= 14:
        min = age - math.ceil(0.1 * age)
        max = age + math.floor(0.1 * age)
    else:
        min = age // 2 + 7
        max = (age - 7) * 2
    return f'{min}-{max}'
