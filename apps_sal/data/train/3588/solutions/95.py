def quadratic(x1, x2):
    a=1
    c=x1*x2
    if x1!=x2:
        b=-(x1+x2)
    if x1==x2:
        b=-2*x1
    return (a,b,c)
