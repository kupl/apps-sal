def digitize(n):
    x = list(map(lambda x: int(x), list(str(n))))
    x.reverse()
    return x
