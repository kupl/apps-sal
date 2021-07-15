def score(n):
    return 0 if n == 0 else n | int(n.bit_length() * '1', 2)
