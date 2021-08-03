def seven(m):
    c = 0
    while(len(str(m))) > 2:
        m = int(str(m)[:-1]) - int(str(m)[-1]) * 2
        c = c + 1
    return (m, c)
