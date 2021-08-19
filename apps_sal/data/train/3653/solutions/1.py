def transform(i):
    return (3 * i - 4 + 2 * (i - 1) * (i - 2), i)


def tops(msg):
    iMax = int((3 + (9 + 8 * len(msg)) ** 0.5) / 4)
    return ''.join((msg[i:i + c] for (i, c) in map(transform, reversed(range(2, iMax + 1)))))
