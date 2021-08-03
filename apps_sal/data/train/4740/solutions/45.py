def row_sum_odd_numbers(n):
    f = ((n * (n - 1)) / 2) - 1
    s1 = (f + 1) * (f + 1)
    s2 = (f + n + 1) * (f + n + 1)
    return s2 - s1
