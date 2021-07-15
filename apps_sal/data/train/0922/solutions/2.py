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
mi     =lambda: map(int,input().split())
mif    =lambda: map(float,input().split())
lii    =lambda: list(map(int,input().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007


#main code
for _ in range(ii()):
    n,m=mi()
    arr=lii()
    brr=lii()
    arr.extend(brr)
    arr.sort()
    d=dd(int)
    for ele in arr:
        d[ele]+=1
    for ele in d:
        if d[ele]==1:
            print(ele,end=' ')
    print()
    
