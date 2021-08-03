def difference_of_squares(n):
    return sum(range(1, n + 1))**2 - sum(map(lambda x: x * x, range(1, n + 1)))
