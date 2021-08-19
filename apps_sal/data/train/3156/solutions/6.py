def even_digit_squares(a, b):
    return [n * n for n in range(1 - int(-a ** 0.5 // 1) & -2, int(b ** 0.5) + 1, 2) if set(str(n * n)) <= set('02468')]
