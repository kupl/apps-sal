def row_sum_odd_numbers(n):
    return sum(n * (n - 1) + 1 + (a * 2) for a in range(n))
