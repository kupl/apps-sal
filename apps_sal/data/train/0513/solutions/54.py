import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000000)

from bisect import bisect_left,bisect_right
n=int(input())
a=list(map(int,input().split()))
G=[[]for i in range(n)]
for i in range(n-1):
  u,v=map(int,input().split())
  G[u-1].append(v-1)
  G[v-1].append(u-1)

lis=[a[0]]
stack=[]
ans=[1]*n
def dfs(cur,p=-1):
  for nx in G[cur]:
    if nx==p:continue
    idx=bisect_left(lis,a[nx])
    if idx==len(lis):
      stack.append((idx,-1))
      lis.append(a[nx])
    else:
      stack.append((idx,lis[idx]))
      lis[idx]=a[nx]
    
    ans[nx]=len(lis)

    dfs(nx,cur)

    idx,v=stack.pop()
    if v<0:
      lis.pop()
    else:
      lis[idx]=v

dfs(0)
print(*ans,sep="\n")
