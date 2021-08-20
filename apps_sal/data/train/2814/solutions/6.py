def is_triangular(n):
    return (-1 + (1 + 8 * n) ** 0.5) / 2 % 1 == 0
