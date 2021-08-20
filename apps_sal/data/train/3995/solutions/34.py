import math


def dating_range(age):
    if age <= 14:
        min = math.floor(age - 0.1 * age)
        max = math.floor(age + 0.1 * age)
        return f'{min}-{max}'
    else:
        min = math.floor(age / 2 + 7)
        max = math.floor((age - 7) * 2)
        return f'{min}-{max}'
