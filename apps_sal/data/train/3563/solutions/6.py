from math import *

def distance(n):
    k=ceil((sqrt(n)-1)/2)
    t=2*k+1
    m=t**2 
    t=t-1
    if n>=m-t: 
        x = k-(m-n),-k   
        return sum(map(abs,x))
    m -= t
    if n>=m-t:
        x = -k,-k+(m-n)  
        return sum(map(abs,x))
    m -= t
    if n>=m-t:
        x =  -k+(m-n),k 
        return sum(map(abs,x))
    x = k,k-(m-n-t)
    return sum(map(abs,x))
