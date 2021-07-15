def get_chance(n, x, a):
    c=0
    r=n-x
    p=1
    while c<a:
        b=r/n
        p=p*b
        r=r-1
        n=n-1
        c=c+1
    return round(p,2)
