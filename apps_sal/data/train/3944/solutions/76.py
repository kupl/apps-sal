def sum_triangular_numbers(n):
    return sum(x * (n - x + 1) for x in range(1, n + 1))
