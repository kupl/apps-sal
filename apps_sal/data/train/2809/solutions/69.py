def digitize(n):
    a = []
    b = str(n)
    for i in b:
        a.append(int(i))
    return a[::-1]
