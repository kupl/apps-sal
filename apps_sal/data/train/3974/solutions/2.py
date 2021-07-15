def two_count(n):
    return n.bit_length() - len(bin(n).rstrip('0')) + 2
