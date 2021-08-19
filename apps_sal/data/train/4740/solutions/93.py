def row_sum_odd_numbers(n):
    return sum([x for x in range(sum(range(1, n)) * 2, sum(range(1, n + 1)) * 2) if x % 2])
