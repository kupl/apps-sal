def fibfusc(n, num_digits=None):
    if n==0: return (1,0)
    x,y=0,1
    trunc=1 if num_digits==None else 10**(num_digits)
    nbin=bin(n)[3:]
    for i in nbin:
        x,y=((x+y)*(x-y),y*(2*x+3*y)) if i=='0' else (-y*(2*x + 3*y),(x + 2*y)*(x + 4*y))
        if trunc > 1 : x,y=(-(-x % trunc),y % trunc)   
    
    return x,y
