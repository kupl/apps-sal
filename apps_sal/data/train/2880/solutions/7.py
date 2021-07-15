def seven(m):
    cnt = 0
    while (m > 99):
        a0 = m % 10
        m = (m - a0) // 10 - 2 * a0
        cnt += 1
    return (m, cnt)
