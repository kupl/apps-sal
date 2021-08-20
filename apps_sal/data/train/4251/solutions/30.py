def difference_of_squares(n):
    a = sum((n for n in range(1, n + 1))) ** 2
    b = sum((n ** 2 for n in range(1, n + 1)))
    return a - b
