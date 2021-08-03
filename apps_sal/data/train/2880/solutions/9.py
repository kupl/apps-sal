def seven(m):
    s = 0
    while m > 99:
        s += 1
        m = (m // 10) - 2 * (m % 10)
    return m, s
