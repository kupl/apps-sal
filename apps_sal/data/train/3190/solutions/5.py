from math import sqrt
def solve(a,b):
    i = a
    s = 0
    while i < b:
        if prope(i):
            s += 1
        i += 1
    return s

def prope(n):    
    return (n*n-n)%100==0 and prime(int(str(n)[:2])) and prime(int(str(n*n)[:2]))

def prime(n):
    if n == 2:
        return True
    i = 2
    while i< sqrt(n)+1:
        if n % i==0:
            return False
        i+=1
    return True
