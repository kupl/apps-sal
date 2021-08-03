def row_sum_odd_numbers(n):
    x = 2 * (sum(list(range(1, n))) + 1) - 1
    num = x
    for i in range(n - 1):
        num += x + 2
        x += 2
    return num
