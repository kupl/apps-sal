def collatz_steps(n, steps):
    a,b,m=1,0,1
    for c in steps:
        if 'U'==c:
            b=3*b+m
            a*=3
        m*=2
    ret=-b*pow(a,m//2-1,m)
    ret+=(n+m-1-ret)//m*m
    return ret

