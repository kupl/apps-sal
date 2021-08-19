def to_binary(n):
    if n < 0:
        return bin(n & 8589934591)[3:]
    return bin(n)[2:]
