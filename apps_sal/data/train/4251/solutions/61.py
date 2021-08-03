def difference_of_squares(n):
    xs = range(1, n + 1)
    return sum(xs)**2 - sum(x * x for x in xs)
