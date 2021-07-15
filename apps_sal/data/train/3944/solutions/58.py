def sum_triangular_numbers(n):
    l = [0]
    for x in range(1, n + 1):
        l.append(x + l[-1])
    return sum(l)
