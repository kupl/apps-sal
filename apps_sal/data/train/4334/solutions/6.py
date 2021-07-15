def skiponacci(n):
    res = []
    a, b = 0, 1

    for i in range(n):
        a, b = a + b, a
        res.append('skip' if i%2 else str(a))

    return ' '.join(res)
