import math


def stringy(size):
    return '10' * math.ceil(size / 2) if size % 2 == 0 else ('10' * math.ceil(size / 2))[:-1]
