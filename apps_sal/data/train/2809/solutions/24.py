def digitize(n):
    b = []
    for i in str(n):
        b.append(int(i))
    return b[::-1]
