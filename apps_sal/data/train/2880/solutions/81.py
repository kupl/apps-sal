def seven(m):
    i = 0
    sm = str(m)
    while len(sm) > 2:
        sm = str(int(sm[:-1]) - 2 * int(sm[-1]))
        i += 1
    return (int(sm), i)

