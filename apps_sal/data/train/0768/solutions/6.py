from sys import setrecursionlimit
setrecursionlimit(999999)
from collections import defaultdict as dd
from collections import deque as dq

def dfs_rec(g,root):
    if len(g[1])==0:
        return [1,1]
    
    sz,mx=1,-1
    
    for i in range(len(g[root])):
        temp = dfs_rec(g,g[root][i])
        sz+=temp[0]
        mx = max(mx,temp[1])
    return [sz,mx+sz]

for _ in range(int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    g = dd(list)
    
    for i in range(n-1):
        g[l[i]].append(i+2)
    
    r = dfs_rec(g,1)[1]
    #print(g)
    print(r+1)
