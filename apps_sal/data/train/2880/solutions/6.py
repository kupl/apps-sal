def seven(m):
    i = 0
    while m >= 100:
        i += 1
        m = m // 10 - m % 10 * 2
    return (m, i)
