def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    (x, y) = (0, 0)
    sum = 0
    for i in range(n):
        x = x + 1
        y = x + y
        sum += y
    return sum
