import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

ii     =lambda: int(input())
si     =lambda: input()
jn     =lambda x,l: x.join(map(str,l))
sl     =lambda: list(map(str,input().strip()))
mi     =lambda: list(map(int,input().split()))
mif    =lambda: list(map(float,input().split()))
lii    =lambda: list(map(int,input().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007


#main code
try:
    n=ii()
    arr=lii()
    for i in range(1,n+1):
        if i!=arr[i-1]:
            l=i
            break
    for i in range(n,-1,-1):
        if i!=arr[i-1]:
            r=i
            break
    temp=arr[l-1:r]
    temp.reverse()
    srr=arr[0:l-1]
    srr.extend(temp)
    srr.extend(arr[r:n])
    if srr==sorted(arr):
        print(l,r)
    else:
        print(0,0)
except:
    print(0,0)
        

