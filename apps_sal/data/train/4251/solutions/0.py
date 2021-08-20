def difference_of_squares(x):
    r = range(1, x + 1, 1)
    return sum(r) ** 2 - sum((z ** 2 for z in r))
