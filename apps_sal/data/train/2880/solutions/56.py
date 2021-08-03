def seven(m):
    steps = 0
    while m // 100 and m > 0:
        m = m // 10 - (2 * (m % 10))
        steps += 1
    return (m, steps)
