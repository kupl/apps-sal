def arr(n=None):
    a = []
    if n is None:
        return a
    else:
        for i in range(n):
            a.append(i)
        return a
