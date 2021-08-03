def fibfusc(n, num_digits=None):
    m = 10 ** num_digits if num_digits is not None else None
    x, y = 1, 0
    for i in reversed(range(n.bit_length())):
        if n & 1 << i == 0:
            x, y = ((x + y) * (x - y), y * (2 * x + 3 * y))
        else:
            x, y = (-y * (2 * x + 3 * y), (x + 2 * y) * (x + 4 * y))
        if m is not None:
            x %= m
            y %= m
    if m is not None and n >= 2:
        x -= m
    return x, y
