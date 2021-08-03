def seven(m, n=0):
    while m > 99:
        n += 1
        m = m // 10 - m % 10 * 2

    return m, n
