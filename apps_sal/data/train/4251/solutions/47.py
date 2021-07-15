def difference_of_squares(n):
    x = sum([i for i in range(1,n+1)])
    return x*x - sum([i*i for i in range(1,n+1)])
