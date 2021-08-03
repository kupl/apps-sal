def to_bytes(n):
    if n == 0:
        return ['00000000']
    s = bin(n)[2:]
    s = s.rjust(len(s) + 7 - (len(s) - 1) % 8, '0')
    return [s[i:i + 8] for i in range(0, len(s), 8)]
