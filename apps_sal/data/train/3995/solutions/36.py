from math import floor


def dating_range(age):
    if age <= 14:
        mn = floor(age - 0.1 * age)
        mx = floor(age + 0.1 * age)
    else:
        mn = age // 2 + 7
        mx = (age - 7) * 2
    return f'{mn}-{mx}'
