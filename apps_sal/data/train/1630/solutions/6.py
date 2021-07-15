import math
from heapq import *
from itertools import combinations

def closure_gen(s):
    keys,seen=set(s),set(s)
    q=sorted(seen)
    while q:
        curr=heappop(q)
        for next in filter(lambda v:not v in seen, [curr+i for i in keys]):
            heappush(q,next)
            seen.add(next)
        yield curr
def gcd(s):
    if len(s)==0:return -1
    if len(s)==1:return s[0]
    res,*s=s
    while s:
        n,*s=s
        res=math.gcd(res,n)
    return res        
    
def survivor(zombies):
    zombies=sorted(set(zombies))
    if not zombies: return -1
    if 1 in zombies: return 0
    if gcd(zombies)>1: return -1
    g=closure_gen(zombies)
    curr=loop=big=0
    zmin=min(zombies)
    while loop<zmin:
        prev,curr=curr,next(g)
        if prev+1==curr:
            loop+=1
        else:
            print(loop,curr)
            loop=0
            big=curr-1
    return big        
