def count_squares(n):
    return n if n < 2 else n ** 2 + count_squares(n - 1)
