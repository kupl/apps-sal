def row_sum_odd_numbers(n):
    if n == 0:
        return 0
    last_odd = n * (n + 1) / 2
    prev_last_odd = (n - 1) * n / 2
    return last_odd * last_odd - prev_last_odd * prev_last_odd
