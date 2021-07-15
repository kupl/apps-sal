def digitize(n):
    rez = []
    for i in list(str(n)[::-1]):
        rez.append(int(i))
    return rez
