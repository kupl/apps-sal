def sum_triangular_numbers(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return (n / 2) * (n + 1) + sum_triangular_numbers(n - 1)
