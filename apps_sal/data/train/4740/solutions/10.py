def row_sum_odd_numbers(n):
    x = []
    for i in range(1, n * n + n, 2):
        x.append(i)
    return sum(x[-n:])
