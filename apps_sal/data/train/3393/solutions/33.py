from math import sqrt

def issquare(x):
    return sqrt(x)==int(sqrt(x))

def list_squared(m, n):
    out_list = []
    for x in range(m,n+1):
        sum_t=sum( (i**2 + (x//i)**2*(x/i!=i) ) for i in range(1,int(sqrt(x))+1) if x % i==0)
        if issquare(sum_t):
            out_list.append([x,sum_t])
    return out_list
