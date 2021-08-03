def row_sum_odd_numbers(n):
    return sum(range(n * (n - 1) + 1, n * (n + 1), 2))
