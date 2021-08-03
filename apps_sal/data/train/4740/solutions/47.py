def row_sum_odd_numbers(n):
    if n == 1:
        return 1
    else:
        min_odd_in_row = (n * (n - 1)) + 1
        max_odd_in_row = (n * (n + 1)) - 1
        return n * (max_odd_in_row + min_odd_in_row) / 2
