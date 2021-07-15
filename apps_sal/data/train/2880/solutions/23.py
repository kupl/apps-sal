def seven(m):
    i = 0
    while m > 99:
        q, r = divmod(m, 10)
        m, i = q - 2 * r, i + 1
    return m, i
