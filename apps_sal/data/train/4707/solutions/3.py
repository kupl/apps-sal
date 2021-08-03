def to_bytes(n):
    b = bin(n)[2:]
    b = '0' * (8 - len(b) % 8) * (len(b) % 8 != 0) + b
    return [b[8 * i:8 * i + 8] for i in range(len(b) // 8)]
