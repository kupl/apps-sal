def row_sum_odd_numbers(n):
    return sum([x * 2 - 1 for x in list(range(n * (n + 1) // 2 - n + 1, n * (n + 1) // 2 + 1))])
