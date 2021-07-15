def seven(m):
    steps = 0
    while m > 99:
        m = m // 10 - 2 * (m % 10)
        steps += 1
    return (m,steps)
