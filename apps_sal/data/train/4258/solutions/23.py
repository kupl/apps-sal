def series_sum(n):
    l=[]
    if n==0:
        x = '0.00'
    while n>0:
        l.append(1/(1+3*(n-1)))
        n-=1
        x = '%.2f' % sum(l)
    return x
