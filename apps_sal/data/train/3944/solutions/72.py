def sum_triangular_numbers(n):
    sum = 0
    i = 0
    tsum = 0
    for row in range(1, n + 1):
        sum = sum + row
        tsum += sum
    return tsum if tsum > 0 else 0
