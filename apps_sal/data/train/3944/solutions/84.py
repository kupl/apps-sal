def sum_triangular_numbers(n):
    return 0 if n < 0 else sum(x * (x + 1) / 2 for x in range(n + 1))
