def row_sum_odd_numbers(n):
    initial_number = n * (n - 1) + 1
    sum = 0
    for i in range(0, n):
        sum = sum + (initial_number + i * 2)
    return sum
