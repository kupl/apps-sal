def encode(s, n):
    return [ord(c) + int(d) - 96 for (c, d) in zip(s, str(n) * len(s))]
