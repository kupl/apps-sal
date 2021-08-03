def seven(m):
    n = 0
    i = 0
    while (m > 99):
        n = m % 10
        m = (m // 10) - 2 * n
        i += 1
    if m % 7 == 0:
        return (m, i)
    else:
        return (m, i)
