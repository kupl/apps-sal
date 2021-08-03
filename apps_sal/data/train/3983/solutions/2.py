def Xbonacci(sig, n):
    res = sig[:n]
    for i in range(n - len(sig)):
        res.append(sum(res[-len(sig):]))
    return res
