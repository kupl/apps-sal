def sum_triangular_numbers(n):
    return 0 if n < 0 else n * (n + 1) * (n + 2) // 6
