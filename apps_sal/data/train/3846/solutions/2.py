def f(k, n):
    if n == 0:
        return 1
    res = 1
    j = 1
    seq = [1]
    for i in range(1,n+1):
        if i%k == 0:
            j = seq[i//k]
        res += j
        seq.append(res)
    return res
