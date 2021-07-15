from bisect import bisect

def pac_man(n,p,es):
    if not es: return n*n-1
    l=len(es)
    y,x=list(map(sorted,list(zip(*es))))
    i=bisect(y,p[0])
    hy=y[i] if i<l else n
    ly=y[i-1] if i>0 else -1
    i=bisect(x,p[1])
    hx=x[i] if i<l else n
    lx=x[i-1] if i>0 else -1
    return (hy-ly-1)*(hx-lx-1)-1

