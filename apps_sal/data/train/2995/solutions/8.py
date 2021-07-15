def sum_mul(n, m):
    L=[]
    if n<=0 or m<=0:
        return 'INVALID'
    else:
        for i in range(0,m):
            if i*n<m:
                L.append(i*n)
        return sum(L)
