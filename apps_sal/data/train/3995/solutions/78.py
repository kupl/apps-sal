from math import floor


def dating_range(age):
    if age <= 14:
        min = floor(age - 0.1 * age)
        max = floor(age + 0.1 * age)
        return '{}-{}'.format(min, max)
    min = age // 2 + 7
    max = (age - 7) * 2
    return '{}-{}'.format(min, max)
