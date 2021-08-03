def row_sum_odd_numbers(n):
    a = ((n - 1)**2) + n
    b = (n**2) + n + 1
    return sum([i for i in range(a, b, 2)])
