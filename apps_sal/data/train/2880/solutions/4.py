def seven(m):
    ctr = 0
    while m >= 100:
        m = m // 10 - 2 * (m % 10)
        ctr += 1
    return (m, ctr)
