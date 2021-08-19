def between(a, b):
    res = []
    while a != b + 1:
        res.append(a)
        a += 1
    return res
