def pyramid(n):
    res = []
    if n != 0:
        for i in range(1,n+1):
            res.append([1 for x in range(i)])
    return res
