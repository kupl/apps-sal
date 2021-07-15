from math import factorial as fac

def xCy(x, y):
    return fac(x) // fac(y) // fac(x - y)
    
def total_inc_dec(x):
    return 1+sum([xCy(8+i,i) + xCy(9+i,i) - 10 for i in range(1,x+1)])

