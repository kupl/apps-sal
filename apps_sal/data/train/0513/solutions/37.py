## まきもどし？
ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
ceil = math.ceil
import sys
sys.setrecursionlimit(10**6)
n = ni()
A = lma()
tree = [[] for i in range(n)]
INF = 10**10
for i in range(n-1):
    u,v = ma();u-=1;v-=1
    tree[u].append(v)
    tree[v].append(u)
#print(tree)
def isok(num,val):##適宜変更
    return num<val
def bisect(ls,val): ##valの関数isok(x,val)がTrueとなる一番右のindex を返す 全部Falseなら-1,Trueならlen(ls)-1
    ok = -1
    ng = len(ls)
    x = (ok+ng)//2
    while ng-ok>1:
        num = ls[x]
        if isok(num,val):
            ok = x
        else:
            ng = x
        x = (ok+ng)//2
    return ok ##一番右のTrueのindex  Trueの個数はok+1こ
def LIS_1(x,ls,right):##right ::これまでわかっている右端
    idx = bisect(ls,x)+1
    if idx+1>right:
        ret= idx+1
    else:
        ret=right
    rewind_idxval.append((idx,ls[idx]))
    ls[idx]=x
    #print(x,ls)
    return ret
def DFS_LIS(prev,ls,right):
    ans[prev]= LIS_1(A[prev],ls,right)
    for node in tree[prev]:
        if not visited[node]:
            visited[node]=True
            DFS_LIS(node,ls,ans[prev])
    #rewind
    idx,pval = rewind_idxval.pop()
    ls[idx] = pval

ans = [0]*n
s = 0
right=0
rewind_idxval=collections.deque()
visited=[False]*n
visited[s]=True
ls=[INF]*n
DFS_LIS(s,ls,right)
#print(ls)
for a in ans :
    print(a)

