from math import floor


def zeros(n):
    sum = 0
    power = 1
    while n / 5**power >= 1:
        sum += floor(n / 5**power)
        power += 1
    return sum
