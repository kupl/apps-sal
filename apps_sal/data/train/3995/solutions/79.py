import math


def dating_range(age):
    if 14 < age <= 100:
        return '%i-%i' % (math.floor(age / 2) + 7, (age - 7) * 2)
    else:
        return '%i-%i' % (math.floor(age - age * 0.1), age + math.floor(age * 0.1))
