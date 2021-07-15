from math import log

def f(z, eps):

    if z==0 or z==1 or (abs(z)**2<min([1,eps])): return 1
    elif abs(z)>=1: return -1
    else: return int(log(eps)/log(abs(z)))
