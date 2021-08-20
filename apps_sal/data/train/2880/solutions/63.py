def seven(m):
    n = 0
    while m // 100 > 0:
        m = m // 10 - 2 * (m % 10)
        n += 1
    return (m, n)
