def sum_triangular_numbers(n):
    return sum(x * (x + 1) / 2 for x in range(n + 1)) if n > 0 else 0
