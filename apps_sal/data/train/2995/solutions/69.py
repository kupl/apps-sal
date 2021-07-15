def sum_mul(n, m):
    if n<=0 or m<=0:
        return 'INVALID'
    elif n==m:
        return 0
    s=0
    for i in range(1,m//n+1):
        if n*i<m:
            s+=n*i
        else:
            break
    return s

