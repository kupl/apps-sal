from math import *


Q = int(input())
data = []
for _ in range(Q):
    A, B = map(int, input().split())
    data.append((A,B))

for A,B in data:
    res = 0
    if A==B==1: print(0)
    else:
        r = floor(((A*B)**(0.5)))
        if r**2==A*B: r-=1
        if (A*B-1)//r==r: res-=1
        if A<=r or B<=r: res-=1
        res += r*2
        print(res)
