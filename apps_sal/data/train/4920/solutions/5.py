from fractions import gcd
from functools import reduce
import math
def min_special_mult(arr):
    a = filter(lambda x:type(x)!=int, [i for i in arr if not str(i).lstrip("-").isdigit() and i!=None])
    arr = [int(i) for i in arr if str(i).lstrip("-").isdigit()]
    if a:
        return "There {} {} invalid entr{}: {}".format("are" if len(a)>1 else "is",len(a),"ies" if len(a)>1 else "y",a if len(a)>1 else a[0])
    return abs(reduce((lambda x,y : x*y/gcd(x,y)),arr))
