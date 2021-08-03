from itertools import cycle


def swap(s, n):
    binary = cycle(bin(n)[2:])
    return ''.join(char.swapcase() if char.isalpha() and next(binary) == '1' else char for char in s)
