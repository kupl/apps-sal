def seven(m):
    m = str(m)
    s = 0
    while len(str(m)) > 2:
        m = int(str(m)[:-1]) - 2 * int(str(m)[-1])
        s += 1
    return(int(m), s)
