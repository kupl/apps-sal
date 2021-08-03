import math


def stringy(size):
    return str('10' * math.ceil(size / 2))[:size]
