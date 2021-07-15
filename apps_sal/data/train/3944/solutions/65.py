def sum_triangular_numbers(n):
    d = 1
    s = 0
    res = 0
    for i in range(n):
        s += d
        res += s
        d += 1
    return res
