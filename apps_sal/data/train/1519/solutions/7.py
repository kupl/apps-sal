import math 
from math import log


def isPowerOfTwo (x):
    return (x and (not(x & (x - 1))) )

n = int(input())
for _ in range(n):
    t = int(input())
    x = int(log(t) / log(2)) + 1
    if t==1:
        print(2)
    else:    
        if not isPowerOfTwo(t):
            print(2**x)
        else:
            print(t)

