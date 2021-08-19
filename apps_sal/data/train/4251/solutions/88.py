def difference_of_squares(n):
    y = sum((i for i in range(1, n + 1)))
    z = sum((i ** 2 for i in range(1, n + 1)))
    return y ** 2 - z
