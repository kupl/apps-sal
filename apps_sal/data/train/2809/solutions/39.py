def digitize(n):
    ls = list(str(n))
    a = ls[::-1]
    return [int(x) for x in a]

