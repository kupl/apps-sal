def sum_triangular_numbers(n):
    if n < 0:
        return 0
    (add, i, l) = (1, 0, [])
    while n != add - 1:
        i += add
        add += 1
        l.append(i)
    sum(l)
    return sum(l)
