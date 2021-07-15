import sys
import math
import heapq
from collections import defaultdict, deque
from decimal import *
input = sys.stdin.readline

def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))

for _ in range(r()):
    n=r()
    already=defaultdict(int)
    res=[]
    sumi=0
    i=1
    len=0
    while len!=n:
        chk=True
        for j in res:
            if already[i+j]==1:
                chk=False
                break
        if chk:
            for j in res:
                already[i+j]=1
            already[i+i]=1
            res.append(i)
            len+=1
        i+=1
    print(*res)
    print(sum(res))
