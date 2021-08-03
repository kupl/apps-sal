def to_bytes(n):
    n = bin(n)[2::]
    while len(n) % 8 != 0:
        n = '0' + n
    return [n[i: i + 8] for i in range(0, len(n), 8)]
