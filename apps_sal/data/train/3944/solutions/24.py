def sum_triangular_numbers(n):
    return 0 if n <= 0 else sum([i for i in range(1, n + 1)]) + sum_triangular_numbers(n - 1)
