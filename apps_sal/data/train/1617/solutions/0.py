from math import *

DIGS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def converter(n, decimals=0, base=pi):
    lst,n = ['-'*(n<0)], abs(n)
    pMax  = max(0, n and int(log(n,base)))
    
    for p in reversed(range(-decimals,pMax+1)):
        if p==-1: lst.append('.')
        p   = base**p
        d,n = n/p, n%p
        lst.append(DIGS[int(d)])
        
    return ''.join(lst)
