def score(n):
    res = n
    while n:
        res, n = res | n, n >> 1
    return res
