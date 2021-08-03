def to_binary(n):
    if n < 0:
        return (bin(n & 0b111111111111111111111111111111111)[3:])
    return bin(n)[2:]
