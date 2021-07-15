def difference_of_squares(x):
    return sum(range(x+1))**2 - sum(i**2 for i in range(x+1))
