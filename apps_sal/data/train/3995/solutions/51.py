import math


def dating_range(age):
    if age > 14:
        a = (age / 2) + 7
        b = (age - 7) * 2
        a = math.floor(a)
        b = math.floor(b)
        return str(a) + "-" + str(b)
    if age <= 14:
        a = age - (0.1 * age)
        b = age + (0.1 * age)
        a = math.floor(a)
        b = math.floor(b)
        return str(a) + "-" + str(b)
