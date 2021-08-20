def to_binary(n):
    n = n & 4294967295
    return bin(n)[2:]
