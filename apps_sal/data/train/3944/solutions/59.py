def sum_triangular_numbers(n):
    t = 1
    s = 0
    for i in range(2, n + 2):
        s = s + t
        t = t + i
    return s
