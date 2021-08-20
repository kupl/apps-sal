def sum_triangular_numbers(n):
    sum = 0
    num = 0
    k = 1
    while n > 0:
        num += k
        sum += num
        k += 1
        n -= 1
    return sum
