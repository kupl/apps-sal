def seven(m):
    step = 0
    n = m
    while n >= 100:
        step += 1
        x, y = divmod(n, 10)
        n = x - 2 * y

    return (n, step)
