from math import ceil


def stringy(size):
    return '0'.join('1' * ceil(size / 2)) + '0' * ((size - 1) % 2)
