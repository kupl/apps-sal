def row_sum_odd_numbers(n):
    row, x = [], 0
    while x < n:
        row.append(n * (n - 1) + 1 + 2 * x)
        x += 1
    return sum(row)
