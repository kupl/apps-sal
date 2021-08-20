def difference_of_squares(n):
    a = 0
    b = 0
    for i in range(1, n + 1):
        a += i
        b += i ** 2
    c = a ** 2
    return c - b
