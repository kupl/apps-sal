def even_fib(m):
    (x, y) = (0, 1)
    counter = 0
    while y < m:
        if y % 2 == 0:
            counter += y
        (x, y) = (y, x + y)
    return counter
