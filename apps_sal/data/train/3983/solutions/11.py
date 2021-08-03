def Xbonacci(signature, n):
    x = len(signature)
    res = signature[:n]

    for i in range(n - x):
        res.append(sum(res[-x:]))

    return res
