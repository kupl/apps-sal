def difference_of_squares(n):
    a = sum([x * x for x in range(1, n + 1)])
    b = sum(range(1, n + 1))
    return (b * b) - a
