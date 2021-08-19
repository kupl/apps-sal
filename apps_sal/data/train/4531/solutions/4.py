def to_binary(n):
    return bin(n & 2 ** 32 - 1)[2:]
