def sum_triangular_numbers(n):
    c, p, g = 0, 0, 1
    for loop in range(n + 1):
        c += p
        p += g
        g += 1
    return c
