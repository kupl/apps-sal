import math


def dating_range(age):
    min = 0
    max = 0
    if age <= 14:
        min = math.floor(age - 0.1 * age)
        max = math.floor(age + 0.1 * age)
    else:
        min = math.floor(age / 2) + 7
        max = 2 * (age - 7)
    return str(min) + '-' + str(max)
