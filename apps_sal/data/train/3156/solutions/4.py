PEDPS = [n * n for n in range(2, 10 ** 6, 2) if set(str(n * n)) <= set('02468')]


def even_digit_squares(a, b):
    return [n for n in PEDPS if a <= n <= b]
