def seven(m):
    c = 0
    while m // 100 != 0:
        m = m // 10 - 2 * (m % 10)
        c = c + 1
    return (m, c)
