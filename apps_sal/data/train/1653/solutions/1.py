def fibfusc(n, num_digits=None):
    if num_digits: mod = pow(10, num_digits)
    x, y = 1, 0
    for c in bin(n)[2:]:
        if c == '0':
            x, y = (x + y) * (x - y), y * ( 2 * x + 3 * y)
        else:
            x, y = -y * (2 * x + 3 * y), (x + 2 * y) * (x + 4 * y)
        if num_digits:
            x, y = x % -mod, y % mod
    return x, y

