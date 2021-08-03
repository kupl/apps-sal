def row_sum_odd_numbers(n):
    row_start = (n - 1) * n + 1
    return sum([x for x in range(row_start, row_start + n * 2, 2)])
