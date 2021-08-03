def seven(m, n=0):
    return (m, n) if m < 100 else seven(int(str(m)[:-1]) - 2 * int(str(m)[-1]), n + 1)
