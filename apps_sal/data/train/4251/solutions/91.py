def difference_of_squares(n):
    x1 = (sum([i for i in range(1, n + 1)])**2)
    x2 = sum([i ** 2 for i in range(1, n + 1)])
    return x1 - x2
