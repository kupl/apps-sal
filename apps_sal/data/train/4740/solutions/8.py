def row_sum_odd_numbers(n):
    sum = 0
    num = n * n + n - 1
    for i in range(n):
        sum += num
        num -= 2
    return sum
