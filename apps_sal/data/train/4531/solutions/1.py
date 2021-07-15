def to_binary(n):
    return bin(n if n >= 0 else 2 ** 32 + n)[2:]
