def seven(m, i=0):
    if m < 100:
        return (m, i)
    return seven(m // 10 - 2 * (m % 10), i + 1)
