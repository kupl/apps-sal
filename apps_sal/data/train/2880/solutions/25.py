def seven(m):
    i = 0
    while len(str(m)) > 2:
        m = int(str(m)[:-1]) - int(str(m)[-1]) * 2
        i += 1
    return (m, i)
