def seven(m):
    i = 0
    while m >= 100:
        m = int(str(m)[:-1]) - 2 * int(str(m)[-1])
        i += 1
    return (m, i)
