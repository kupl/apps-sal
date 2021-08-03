def convert_bits(a, b):
    difference = bin(a ^ b)[2:]
    return difference.count("1")
