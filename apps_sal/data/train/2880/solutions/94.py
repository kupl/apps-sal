def seven(m):
    y = 0
    while m // 100 != 0:
        if m < 0:
            return (m, y)
        y += 1
        m = m // 10 - m % 10 * 2
    return (m, y)
