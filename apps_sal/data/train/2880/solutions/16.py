def seven(m):
    steps = 0
    while len(str(m)) > 2:
        m = (m // 10) - (2 * (m % 10))
        steps += 1
    return (m, steps)
