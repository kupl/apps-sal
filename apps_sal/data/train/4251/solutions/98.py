def difference_of_squares(n):
    return abs(sum(x**2 for x in range(1,n+1)) - sum(x for x in range(1,n+1))**2)
