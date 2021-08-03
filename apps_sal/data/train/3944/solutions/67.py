def sum_triangular_numbers(n):
    l = []
    c = 0
    for i in range(1, n + 1):
        c += i
        l.append(c)
    return sum(l)
