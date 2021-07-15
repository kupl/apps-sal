def difference_of_squares(n):
    print(n)
    a = sum(range(n + 1)) ** 2
    b = sum([(i+1)**2 for i in range(n)])
    return a - b

