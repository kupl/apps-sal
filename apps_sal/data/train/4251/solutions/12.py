def difference_of_squares(n):
    return sum(range(n + 1))**2 - sum(i**2 for i in range(n + 1))
