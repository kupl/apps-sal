def fibfusc(n, num_digits=None):

    def f0(x, y):
        return ((x + y) * (x - y), y * (2 * x + 3 * y))

    def f1(x, y):
        return (-y * (2 * x + 3 * y), (x + 2 * y) * (x + 4 * y))
    (x, y) = (1, 0)
    if num_digits:
        m = 10 ** num_digits
    for digit in bin(n)[2:]:
        if digit == '0':
            (x, y) = f0(x, y)
        else:
            (x, y) = f1(x, y)
        if num_digits:
            (x, y) = (x % m - m, y % m)
    return (x, y)
