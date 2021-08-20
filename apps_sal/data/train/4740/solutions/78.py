def row_sum_odd_numbers(n):
    start = n ** 2 - n + 1
    stop = start + n * 2
    return sum((x for x in range(start, stop, 2)))
