def digitize(n):
    n = str(n)
    n = n[::-1]
    res = []
    for i in n:
        res.append(int(i))

    return res
