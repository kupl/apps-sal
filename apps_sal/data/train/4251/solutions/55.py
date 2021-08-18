def difference_of_squares(n):
    a, b = 0, 0
    for x in range(1, n + 1):
        a += x
        b += x ** 2
    return a ** 2 - b
