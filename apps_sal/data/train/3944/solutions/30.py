def sum_triangular_numbers(n):
    increment = 1
    sum_ = 0
    number = 0
    while increment <= n:
        number += increment
        sum_ += number
        increment += 1
    return sum_
