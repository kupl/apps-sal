from functools import reduce
from math import gcd
def sieve(n):
    start = int(n**0.5) +2
    arr =[True]*(n+1)
    primes= []
    for i in range(2,start):
        if arr[i]==True:
            primes.append(i)
        for j in range(i*2,n+1,i):
            arr[j]=False
    #saved till start primes now saving from start till n
    for i in range(start,n+1):
        if arr[i] ==True:
            primes.append(i)
    return primes
def divs(n,primes):
    sq= n**0.5
    fac =[]
    for i in primes:
        if i > sq:
            break
        if n%i==0:
            fac.append(i)
    if len(fac)==0:
        fac = [n]
    return fac
primes =sieve(int((10**5)**0.5+1))
#print(primes)
for _ in range(int(input())):
    n = int(input())
    ls = [int(X)  for X in input().split()]
    gc = reduce(gcd,ls)
    x = divs(gc,primes)
    if x[0]!=1:
        print(x[0])
    elif x[0]==1 and len(x)>1:
        print(x[1])
    else:print(-1)











    #gcd gives you the greatest common divisor simply printing this is incorrect
    #since gcd divides all the numbers in the array it's divisors will also do the same
    #find the smallest divisor (smallest prime)
