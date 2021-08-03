def int_to_negabinary(i):
    return '{:b}'.format((0xAAAAAAAA + i) ^ 0xAAAAAAAA)


def negabinary_to_int(n):
    return (int(n, 2) ^ 0xAAAAAAAA) - 0xAAAAAAAA
