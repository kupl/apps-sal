def sum_triangular_numbers(n):
    return sum((i * 0.5 * (i + 1) for i in range(n + 1)))
