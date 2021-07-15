import sys
sys.setrecursionlimit(10**6)
f=lambda:map(int,input().split())
n,m=f()
g=[[] for _ in range(n)]
for _ in range(m):
  u,v,l=f()
  g[u-1]+=[(v-1,l)]
  g[v-1]+=[(u-1,l)]
a=[0]*n
def dfs(v,p=-1,l=1):
  a[v]=l
  for c,m in g[v]:
    if c==p or a[c]: continue
    if l==m: m=1+(m==1)
    dfs(c,v,m)
dfs(0)
print(*a,sep='\n')
