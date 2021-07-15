from collections import Counter
from functools import reduce
from operator import mul
from random import randrange,randint

def primesbelow(n):
    c=n%6>1
    n={0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    s=[True]*(n//3)
    s[0]=False
    for i in range(int(n**0.5)//3+1):
        if s[i]:
            k=(3*i+1)|1
            s[k*k//3::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
            s[(k*k+4*k-2*k*(i%2))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i%2))//6-1)//k+1)
    return [2,3]+[(3*i+1)|1 for i in range(1,n//3-c) if s[i]]

medsize=100000
medprimes=set(primesbelow(medsize))
smallprimes=sorted(p for p in medprimes if p<1000)

def isprime(n,precision=7):
    if n<1:
        return False
    elif n<=3:
        return n>=2
    elif n%2==0:
        return False
    elif n<medsize:
        return n in medprimes
    d=n-1
    s=0
    while d%2==0:
        d//=2
        s+=1
    for repeat in range(precision):
        a=randrange(2,n-2)
        x=pow(a,d,n)
        if x==1 or x==n-1: continue
        for r in range(s-1):
            x=pow(x,2,n)
            if x==1: return False
            if x==n-1: break
        else: return False
    return True

def pollard_brent(n):
    if n%2==0: return 2
    if n%3==0: return 3
    y,c,m=randint(1,n-1),randint(1,n-1),randint(1,n-1)
    g,r,q=1,1,1
    while g==1:
        x=y
        for i in range(r): y=(pow(y,2,n)+c)%n
        k=0
        while k<r and g==1:
            ys=y
            for i in range(min(m,r-k)):
                y=(pow(y,2,n)+c)%n
                q=q*abs(x-y)%n
            g=gcd(q,n)
            k+=m
        r*=2
    if g==n:
        while True:
            ys=(pow(ys,2,n)+c)%n
            g=gcd(abs(x-ys),n)
            if g>1: break
    return g

def primefactors(n):
    fs=[]
    for c in smallprimes:
        while n%c==0:
            fs.append(c)
            n//=c
        if c>n: break
    if n<2: return fs
    while n>1:
        if isprime(n):
            fs.append(n)
            break
        f=pollard_brent(n)
        fs.extend(primefactors(f))
        n//=f
    return fs

def factorization(n):
    return Counter(primefactors(n))

def ssd(n):
    return reduce(mul,((p**(2*e+2)-1)//(p*p-1) for p,e in factorization(n).items()),1)

def list_squared(m,n):
    return [a for a in ([x,ssd(x)] for x in range(m,n+1)) if (a[1]**0.5).is_integer()]
