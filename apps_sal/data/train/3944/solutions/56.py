def sum_triangular_numbers(n):
    return sum([sum([y for y in range(1, x + 1)]) for x in range(1, n + 1)])
