def sum_triangular_numbers(n):
    s = 1
    x = []
    for i in range(2, n + 2):
        x.append(s)
        s += i

    return sum(x)
