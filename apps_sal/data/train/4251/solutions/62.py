def difference_of_squares(n):
    return sum(range(0, n + 1)) ** 2 - sum((x ** 2 for x in range(0, n + 1)))
