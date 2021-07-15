def convert_bits(a, b):
    n = a ^ b
    c = 0
    while n:
        c += n & 1
        n >>= 1
    return c
