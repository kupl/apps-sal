def count_by(x, n):
    x1 = x
    res = []
    for i in range(n):
        res.append(x)
        x += x1
    return res
