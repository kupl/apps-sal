def sum_triangular_numbers(n):
    return 0 if n < 0 else sum(k * (k + 1) // 2 for k in range(1, n + 1))
