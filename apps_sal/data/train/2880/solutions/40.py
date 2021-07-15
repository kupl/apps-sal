def seven(m):
    steps = 0
    while len(str(m)) > 2:
        strm = str(m)
        lastdigit = 2 * int(strm[-1])
        m = int(strm[:-1]) - lastdigit
        steps += 1
    return (m, steps)

