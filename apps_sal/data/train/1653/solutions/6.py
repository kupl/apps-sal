def fibfusc(n, num_digits=None):
    x, y = 1, 0
    for k in range(len(bin(n)) - 3, - 1, -1):
        m = n >> k
        if m & 1:
            x, y = -y * (2 * x + 3 * y), (x + 2 * y) * (x + 4 * y)
        else:
            x, y = (x + y) * (x - y), y * (2 * x + 3 * y)
        if num_digits:
            x, y = x % 10 ** num_digits, y % 10 ** num_digits
    if num_digits and n > 1:
        x -= 10 ** num_digits
    return x, y
