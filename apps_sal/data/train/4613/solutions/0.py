def binary_string_to_int(string):
    return sum((d == '1') * 2**i for i, d in enumerate(string[::-1]))


def add(a, b):
    return '{:b}'.format(binary_string_to_int(a) + binary_string_to_int(b))
