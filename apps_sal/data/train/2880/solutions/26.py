def seven(m, steps=0):
    if m / 100 < 1:
        return (m, steps)
    else:
        return seven(m // 10 - 2 * (m % 10), steps + 1)
