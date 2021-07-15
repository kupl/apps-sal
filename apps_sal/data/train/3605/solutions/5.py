from functools import reduce 
def comb(n, p):
    a,b = n-p, p
    return reduce(lambda x, y : x*y, range(max(a,b)+1,n+1))//reduce(lambda x, y : x*y, range(1,min(a,b)+1))

def diagonal(n, p):
    return comb(n+1, p+1)
