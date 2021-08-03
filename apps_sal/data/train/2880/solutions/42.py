def seven(m):
    counter = 0
    while m >= 99:
        m = m // 10 - 2 * (m % 10)
        counter += 1
    return (m, counter)
