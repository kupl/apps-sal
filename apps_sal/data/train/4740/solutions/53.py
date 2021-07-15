def row_sum_odd_numbers(n):
    start = 1
    for z in range(n):
        start += 2 * z
    sum_of_odd = 0
    for i in range(1, n + 1):
        sum_of_odd += start
        start += 2
    return sum_of_odd
