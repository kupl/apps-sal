def count_sheep(n):
    res=''
    for p in range(1,n+1):
        p=str(p)
        res=res + (p + ' sheep...')
    return res
