def convert_bits(a, b):
    return list(bin(a ^ b)).count('1')
