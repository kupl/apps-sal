def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    return round((1 / 6 * n**3) + (1 / 2 * n**2) + (1 / 3 * n), 0)
