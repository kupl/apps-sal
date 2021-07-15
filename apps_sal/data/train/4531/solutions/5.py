def to_binary(n):
    n = n & 0xFFFFFFFF
    return bin(n)[2:]
