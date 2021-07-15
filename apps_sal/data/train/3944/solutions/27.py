def sum_triangular_numbers(n):
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += sum(range(1, i + 1))
    return sum_

