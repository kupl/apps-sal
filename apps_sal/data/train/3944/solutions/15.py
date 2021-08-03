def sum_triangular_numbers(n):
    total = 0
    x = 0
    for i in range(1, n + 1):
        x += i
        total += x
    return total
