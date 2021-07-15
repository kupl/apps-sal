def reverse_bits(n):
    return int(''.join(reversed(bin(n)[2:])), 2)
