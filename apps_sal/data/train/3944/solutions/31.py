def sum_triangular_numbers(n, c=1, v=2):
    return c + sum_triangular_numbers(n-1, c + v, v+1) if n > 0 else 0
