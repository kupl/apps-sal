def difference_of_squares(n):
    return sum(n - i for i in range(0, n))**2 - sum((n - i)**2 for i in range(0, n))
