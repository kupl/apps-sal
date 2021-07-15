from math import factorial,pi
from fractions import Fraction

def comb(n,k):
    return factorial(n)//(factorial(n-k)*factorial(k))

def bernoulli(m):
    b=[1]
    for i in range(1,m+1):
        n=0
        for k in range(0,i):
            n+=comb(i+1,k)*b[k]
        b.append(Fraction(-n,i+1))
    return b

b=bernoulli(31)

def series(k, nb) :
    if k<0:
        k=-k
        return (b[k+1]*(-1)**k)/(k+1)
    elif k%2==1:
        return sum(1/(n**k) for n in range(1,nb+1))
    else:
        return abs(b[k])*((2*pi)**k)/(2*factorial(k))
