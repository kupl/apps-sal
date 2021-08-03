def digitize(n):
    a = list(reversed(str(n)))
    k = []
    for i in a:
        k.append(int(i))
    return k
