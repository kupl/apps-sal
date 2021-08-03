from math import floor


def dating_range(age):

    if age > 14:
        min = age / 2 + 7
        max = (age - 7) * 2
    else:
        min = age - 0.10 * age
        max = age + 0.10 * age

    return f'{floor(min)}-{floor(max)}'
