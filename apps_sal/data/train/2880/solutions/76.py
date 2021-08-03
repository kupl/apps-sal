def seven(m, step=0):
    while m > 99:
        a = int(m / 10)
        b = m - (a * 10)
        m = a - (2 * b)
        step += 1
    return m, step
