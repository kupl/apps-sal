def row_sum_odd_numbers(n):
    start = 0
    sum = 0
    for i in range(n - 1):
        start += i + 1
    start = start * 2 + 1
    for i in range(n):
        sum += start
        start += 2
    return sum
