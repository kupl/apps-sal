def shared_bits(a, b):
    return bin(a & b).count('1') > 1
