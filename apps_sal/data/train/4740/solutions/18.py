def row_sum_odd_numbers(n):
    stop = sum(range(n + 1))
    start = sum(range(n)) + 1
    return sum(range(start + start - 1, stop + stop, 2))
