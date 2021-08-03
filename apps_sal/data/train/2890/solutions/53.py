def multiples(m, n):
    res = []
    for i in range(1, m + 1):
        val = n * i
        res.append(val)
    return res
