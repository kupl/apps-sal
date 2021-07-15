def digitize(n):
    return list(int(x) for x in str(n)[::-1])
