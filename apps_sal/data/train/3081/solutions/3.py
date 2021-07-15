import random

def squares(n):
        return [i*i for i in range(1,n+1)]

def num_range(n, start, step):
    return [ i for i in range(start,start+n*step,step) ]

def rand_range(n, mn, mx):
    return [ random.randint(mn, mx) for nvm in range(n) ]

def primes(n):
    if n ==1:
        return [2]
    if n ==2:
        return [2,3]
    c = 2
    ReturnLs = [2,3]
    i = 5
    while c<n:
        if isprime(i):
            ReturnLs.append(i)
            c+=1
        i+=2
    return ReturnLs
def isprime(n):
    if n%2==0:
        return False
    if n%3==0:
        return False
    for i in range(5,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
