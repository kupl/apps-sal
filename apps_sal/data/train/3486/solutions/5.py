def find_last(n, m):
    pp=list(range(1,n+1))
    p=0
    while len(pp)>1:
        p=(p+m-1)%len(pp)
        del pp[p]
    s=(n-1)*m+(n-m)*(n-m+1)
    return pp[0],s
