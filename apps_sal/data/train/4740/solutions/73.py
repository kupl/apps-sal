def row_sum_odd_numbers(n):
    start_number = n ** 2 - (n - 1)
    sum = 0
    for i in range(n):
        sum += start_number + i * 2
    return sum
