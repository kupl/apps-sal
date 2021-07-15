def climb(n):
    r=[n]
    while(n>1):
        if n%2==0:
            n//=2
        else:
            n=(n-1)//2
        r.append(n)
    return r[::-1]

def fibfusc(n, num_digits=None):
    if n==0: return (1,0)
    r=climb(n)
    x,y=0,1
    for i in r[1:]:
        if i%2==0:
            if num_digits:
                x,y=((x+y)%(10**num_digits))*(x-y), y*((2*x+3*y)%(10**num_digits))
            else:
                x,y=(x+y)*(x-y), y*(2*x+3*y)
        else:
            if num_digits:
                x,y=-y*((2*x+3*y)%(10**num_digits)), (x+2*y)*(x+4*y)
            else:
                x,y=-y*(2*x+3*y), (x+2*y)*(x+4*y)
        if num_digits:
            x=x%(10**num_digits) if x>=0 else -(abs(x)%(10**num_digits))
            y=y%(10**num_digits)
    return (x,y)
