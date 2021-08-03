from math import floor


def dating_range(age):
    if age <= 14:
        min = floor(age - 0.1 * age)
        max = floor(age + 0.1 * age)
        return f'{min}-{max}'
    return f'{floor(age//2+7)}-{floor((age-7)*2)}'
