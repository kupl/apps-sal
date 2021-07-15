def convert_bits(a, b):
    return str(bin(a ^ b)).count('1')
