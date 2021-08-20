def difference_of_squares(n):
    size = range(1, n + 1)
    return sum((x for x in size)) ** 2 - sum((x ** 2 for x in size))
