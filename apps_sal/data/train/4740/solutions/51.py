def row_sum_odd_numbers(n):
    num1 = n * (n - 1)
    num1 += 1
    i = 0
    sum = 0
    while i < n:
        num2 = 0
        num2 = num1 + i * 2
        sum += num2
        i += 1
    return sum
