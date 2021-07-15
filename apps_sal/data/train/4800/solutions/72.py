def hotpo(n):
    x=0
    while n>1:
        if n%2==0:
            n/=2
            x+=1
        else:
            n=3*n+1
            x+=1
    return x
