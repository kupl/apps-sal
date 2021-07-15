import bisect
import sys
sys.setrecursionlimit(10**7)

def dfs(v):
    pos=bisect.bisect_left(dp,arr[v])
    changes.append((pos,dp[pos]))
    dp[pos]=arr[v]
    ans[v]=bisect.bisect_left(dp,10**18)
    for u in g[v]:
        if checked[u]==0:
            checked[u]=1
            dfs(u)
    pos,val=changes.pop()
    dp[pos]=val


n=int(input())
arr=[0]+list(map(int,input().split()))
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
ans=[0]*(n+1)
checked=[0]*(n+1)
checked[1]=1
dp=[10**18 for _ in range(n+1)]
changes=[]
dfs(1)
for i in range(1,n+1):
    print(ans[i])
