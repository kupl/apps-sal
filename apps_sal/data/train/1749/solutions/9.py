from gmpy2 import is_prime,next_prime
def trailing_zeros(n,b):
    F,p=[],1
    while 1<b:
        p,c=next_prime(p),0
        while b%p==0:b,c=b//p,c+1
        F+=[(p,c)]*(0<c)
        if is_prime(b):F,b=F+[(b,1)],1
    Z=[]
    for e,c in F:
        m,t=n,0
        while 1<m:
            m,_=divmod(m,e)
            t+=m
        Z+=[t//c]
    return min(Z)
