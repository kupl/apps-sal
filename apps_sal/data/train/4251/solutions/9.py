def difference_of_squares(n):
    return sum(range(n + 1)) ** 2 - sum(map(lambda x: x ** 2, range(n + 1)))
