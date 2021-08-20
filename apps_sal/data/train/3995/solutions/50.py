from math import ceil


def dating_range(age):
    if age <= 14:
        return f'{age - ceil(age / 10)}-{age + int(age / 10)}'
    return f'{age // 2 + 7}-{2 * (age - 7)}'
