def sum_triangular_numbers(n):
    result = 0
    x = 0
    for y in range(n + 1):
        x += y
        result += x
    return result
