def sum_triangular_numbers(n):
    if n < 1:
        return 0
    total = 0
    a = 0
    for i in range(0, n):
        a += i + 1
        total += a
    return total
