def difference_of_squares(n):
    a, b = 0, 0
    for x in range(1, n + 1):
        a += x
    for x in range(1, n + 1):
        x = x ** 2
        b += x
    return a ** 2 - b
    # Flez
