def zeros(n):
    c=0;r=1
    while 5**r<=n:c+=len(range(5**r,n+1,5**r));r+=1
    return c
