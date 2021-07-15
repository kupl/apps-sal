def digitize(n):
    l = []
    m = []
    n = str(n)
    n = n[::-1]
    for i in range(len(n)):
        l.append(int(n[i]))
    return l
