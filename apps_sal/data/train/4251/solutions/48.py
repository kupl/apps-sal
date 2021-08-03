def difference_of_squares(n):
    r = list(range(n + 1))
    return sum(r)**2 - sum([x**2 for x in r])
