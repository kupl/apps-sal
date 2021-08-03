def row_sum_odd_numbers(n):
    row_start_num = (n - 1) * n + 1
    row_sum = n * row_start_num + n * (n - 1)
    return row_sum
