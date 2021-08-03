from math import floor


def dating_range(age):
    if age <= 14:
        return f'{floor(age - (0.1 * age))}-{floor(age + (0.1 * age))}'
    else:
        return f'{floor((age/2) + 7)}-{floor((age-7) * 2)}'
