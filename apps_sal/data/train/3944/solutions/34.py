def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    total = 0
    for num in range(n+1):
        triangle_num = num * (num + 1) / 2
        total = total + triangle_num
    return total

