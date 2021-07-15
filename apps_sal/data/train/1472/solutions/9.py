# Coder : Hakesh D #
import sys
#input=sys.stdin.readline

from collections import deque
from math import ceil,sqrt,gcd,factorial
from bisect import bisect_right,bisect_left

mod = 1000000007
INF = 10**18
NINF = -INF
def I():return int(input())
def MAP():return map(int,input().split())
def LIST():return list(map(int,input().split()))
def modi(x):return pow(x,mod-2,mod)
def lcm(x,y):return (x*y)//gcd(x,y)
def write(l):
    for i in l:
        print(i,end=' ') 
    print()
########################################################################################
n = int(input())
ans = out = 0
for i in range(1,1000000):
    p = 1
    pres = 0
    while(i != 0):
        digit = i % 10
        if(digit == 1):pres = 1
        p *= digit
        i = i//10
    if(p == n and pres == 0):ans+=1
    if(p == n and pres == 1):out+=1

print(ans,out)



