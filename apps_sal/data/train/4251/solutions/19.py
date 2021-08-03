def difference_of_squares(n):
    a = sum([i for i in range(1, n + 1)])**2
    b = sum([i**2 for i in range(1, n + 1)])
    return a - b
