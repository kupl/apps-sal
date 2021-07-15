# cook your dish here
# Let's hack this code.

from sys import stdin, stdout
import math
from itertools import permutations, combinations
from collections import defaultdict
from bisect import bisect_left 

mod = 1000000007

def L():
    return list(map(int, stdin.readline().split()))

def In():
    return map(int, stdin.readline().split())

def I():
    return int(stdin.readline())

def printIn(ob):
    return stdout.write(str(ob)+'\n')

def powerLL(n, p):
    result = 1
    while (p):
        if (p&1):
            result = result * n % mod
        p = int(p / 2)
        n = n * n % mod
    return result

#--------------------------------------

def myCode():
    ext = 0
    short = 0
    s,n,k,r = In()
    share = k
    dist = k
    for i in range(n-1):
        dist = dist*r
        share = share + dist
    if share <= s:
        ext = s-share
        print("POSSIBLE "+str(ext))
    else:
        short = share-s
        print("IMPOSSIBLE "+str(short))
        
    return ext,short

def main():
    extra = 0
    shortage = 0
    for t in range(I()):
        e,s = myCode()
        extra +=e
        shortage += s
    if extra >=shortage:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    
def __starting_point():
    main()
__starting_point()
