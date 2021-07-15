from fractions import Fraction 
from decimal import *

def count_sixes(n):
    a = 6 << (n - 2)
    b = Fraction(2,3)
    c = Fraction(1,a) 
    d = 0 
    if n % 2 == 0:
        d = b - c 
    else:
        d = b + c     
    getcontext().prec = 100000
    e = str(Decimal(d.numerator)/Decimal(d.denominator))
    f = 0     
    for i in range(2,len(e)):
        if e[i] == '6': 
            f += 1
        else: break 
    return f

