import math 
from math import pi 
def comb(n,k):
    return(math.factorial(n)/math.factorial(n-k)/math.factorial(k))

def bernoulli():
    A=[1]
    yield A[0]
    counter=0;
    while True:
        somma=0
        p=len(A)
        for i in range(len(A)):
            somma+=A[i]*comb(p+1,i)/(p+1)
        A.append(-somma)
        if (len(A)<4 or len(A)%2==1):
            counter+=1
            yield A[counter]
    

def series(k, nb) :
    if (k%2==1 and k>2):
        return sum(map(lambda x:1/(x**k), range(1,nb+1)))
    bn2 = [ix for ix in zip(range(abs(k)+2), bernoulli())]
    bn2 = [b for i,b in bn2]
    if (k%2==0 and k>=2):
        return 1/2*abs(bn2[k])*(2*pi)**k/math.factorial(k)
    else:
        k=abs(k)
        return ((-1)**k*bn2[k+1]/(k+1))
