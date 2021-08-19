from math import floor


def dating_range(age):
    if age > 14:
        min = age / 2 + 7
        max = (age - 7) * 2
        return '{}-{}'.format(floor(min), floor(max))
    elif age <= 14:
        min = age - 0.1 * age
        max = age + 0.1 * age
        return '{}-{}'.format(floor(min), floor(max))
