def sum_triangular_numbers(n):
    return [0, (n**3 - n) / 6 + .5 * n * (n + 1)][n > 0]
