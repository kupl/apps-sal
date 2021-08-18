def row_sum_odd_numbers(n):
    m = (n - 1) * n + 1
    o = m
    while n > 1:
        m = m + 2
        o = o + m
        n = n - 1
    return o
