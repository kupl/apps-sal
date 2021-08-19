import math


def dating_range(age):
    if age >= 14:
        max = (age - 7) * 2
        min = age / 2 + 7
    else:
        min = age - 0.1 * age
        max = age + 0.1 * age
    return str(math.floor(min)) + '-' + str(math.floor(max))
