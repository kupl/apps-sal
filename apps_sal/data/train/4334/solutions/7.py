def skiponacci(n):
    res = []
    (a, b) = (0, 1)
    for i in range(n):
        (a, b) = (a + b, a)
        if i % 2:
            res.append('skip')
        else:
            res.append(str(a))
    return ' '.join(res)
