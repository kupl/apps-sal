def fibfusc(n, num_digits=None):
    if num_digits:
        num_digits = 10 ** num_digits
    x, y = 1, 0
    for c in bin(n)[2:]:
        if c == '1':
            x, y = -y * (2 * x + 3 * y), (x + 2 * y) * (x + 4 * y)
        else:
            x, y = (x + y) * (x - y), y * (2 * x + 3 * y)
        if num_digits:
            x, y = x % -num_digits, y % num_digits
    return x, y
