def difference_of_squares(n):
    a = sum([x * x for x in range(1, n + 1)])
    # print(a)
    b = sum(range(1, n + 1))
    # print(b)
    return (b * b) - a
