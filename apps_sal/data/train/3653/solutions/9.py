def tops(msg):
    return ''.join((msg[n * (2 * n - 3):2 * n * (n - 1)] for n in range(int((3 + (9 + 8 * len(msg)) ** 0.5) / 4), 1, -1)))
