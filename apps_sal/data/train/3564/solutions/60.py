from math import ceil


def stringy(size):
    return '10' * (size // 2) if size % 2 == 0 else str('10' * ceil(size / 2))[:-1]
