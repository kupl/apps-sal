def seven(m):
    i = 0
    while len(str(m)) > 2:
        i += 1
        m = int(str(m)[:-1]) - 2 * int(str(m)[-1])
    return (m, i)
