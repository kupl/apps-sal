def difference_of_squares(n):
    return sum(range(1, n + 1))**2 - sum(map(lambda a: a**2, range(1, n + 1)))
