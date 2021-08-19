def difference_of_squares(n):
    a = sum(list(range(1, n + 1))) ** 2
    b = sum([i ** 2 for i in list(range(1, n + 1))])
    return abs(a - b)
