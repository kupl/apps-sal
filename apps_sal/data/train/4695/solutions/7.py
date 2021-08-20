def count_squares(n):
    return count_squares(n - 1) + n ** 2 if n > 0 else 0
