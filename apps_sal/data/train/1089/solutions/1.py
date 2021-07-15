from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)




def dfs(node):
 visited[node]=True
 n0[node]+=1
 for x in d[node]:
  if visited[x]==False:
   dfs(x)
   n0[node]+=n0[x]
def dfs1(node):
 nonlocal ans
 visited[node]=True
 co=0
 for x in d[node]:
  if visited[x]==False:

   dfs1(x)
   if n0[x]==1:
    co+=1

 ans1=co//3
 ##print(ans1,node)
 if 3*ans1==len(d[node]):
  n0[node]=1
  ##print(n0[node],node)
 ans-=3*ans1





for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 d=defaultdict(list)
 ans=n
 for i in range(len(a)):
  d[a[i]].append(i+2)
 ##print(d)
 visited = [False] * (n + 1)
 n0 = [0] * (n + 1)
 ##print(n0)
 dfs(1)
 ## print(n0)
 visited=[False]*(n+1)
 dfs1(1)
 print(ans)




