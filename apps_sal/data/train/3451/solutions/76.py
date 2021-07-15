import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  
    
def triangle(row):
    dict = {'R':0, 'G':1, 'B':2}
    dict2 = {0:'R', 1:'G', 2:'B'}
    if len(row) % 2 == 0:
        x = -1
    else:
        x = 1
    sum = 0
    n = len(row)-1
    k = 0
    for i in row:
        sum += ncr(n, k)*dict[i]
        print(ncr(n, k), dict[i])
        k+=1
    return dict2[x*sum % 3]
