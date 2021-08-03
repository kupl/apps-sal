def difference_of_squares(x):
    return sum(i for i in range(1, x + 1))**2 - sum(i**2 for i in range(1, x + 1))
