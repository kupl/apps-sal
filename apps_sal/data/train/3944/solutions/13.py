def sum_triangular_numbers(n):
    if n > 0:
        return sum([x * (x + 1) / 2 for x in range(n + 1)])
    else:
        return 0
