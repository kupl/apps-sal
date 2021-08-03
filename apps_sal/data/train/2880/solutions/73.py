def seven(m):
    n, i = m, 0
    while n >= 100:
        n, i = n // 10 - 2 * int(str(n)[-1]), i + 1
    return (n, i)
