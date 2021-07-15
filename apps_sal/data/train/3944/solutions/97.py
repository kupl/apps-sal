def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    result_sum = 0
    exponent = 2
    num = 1
    for _ in range(n - 1):
        num = num + exponent
        exponent += 1
        result_sum += num
    return result_sum + 1
