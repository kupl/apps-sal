def sum_triangular_numbers(n):
    return sum(i * (i + 1) / 2 for i in range(1, n + 1)) if n > 0 else 0
