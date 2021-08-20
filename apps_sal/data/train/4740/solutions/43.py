def row_sum_odd_numbers(n):
    a = sum(range(1, n)) * 2 + 1
    return sum(range(a, a + n * 2, 2))
