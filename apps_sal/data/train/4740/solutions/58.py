def row_sum_odd_numbers(n):
    k = sum(range(n))
    count = 0
    start = 1 + k * 2
    sum_i = 0
    while count < n:
        sum_i += start
        start += 2
        count += 1
    return sum_i
