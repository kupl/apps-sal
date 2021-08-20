def difference_of_squares(n):
    sum_square = 0
    sum_numbers = 0
    for i in range(1, n + 1):
        sum_square += i ** 2
    for i in range(1, n + 1):
        sum_numbers += i
    squared = sum_numbers ** 2
    return squared - sum_square
