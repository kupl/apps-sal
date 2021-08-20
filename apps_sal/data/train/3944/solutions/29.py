def sum_triangular_numbers(n):
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += (i ** 2 + i) // 2
    return sum_
