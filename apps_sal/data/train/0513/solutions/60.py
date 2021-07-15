from bisect import bisect_left as bl
import sys
sys.setrecursionlimit(10**6)
n=int(input())
a=list(map(int,input().split()))
t=[[]for i in range(n)]
for i in range(n-1):
    u,v=list(map(int,input().split()))
    t[u-1].append(v-1)
    t[v-1].append(u-1)
b=[0]*n
dp=[float("inf")]*n
def f(c,d):
    h=bl(dp,a[c])
    g=dp[h]
    dp[h]=min(dp[h],a[c])
    b[c]=bl(dp,float("INF"))
    for i in t[c]:
        if i!=d:f(i,c)
    dp[h]=g
f(0,-1)
for i in b:
    print(i)

