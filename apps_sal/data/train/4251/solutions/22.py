def difference_of_squares(n):
    n1 = sum(range(1, n + 1))
    
    return n1 * n1 - sum([i * i for i in range(1, n + 1)])
