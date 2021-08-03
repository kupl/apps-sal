def sum_triangular_numbers(n):
    c, l = 0, 0
    for i in range(1, n + 1):
        l = l + i
        c += l
    return c
