# cook your dish here
t=int(input())
import sys
sys.setrecursionlimit(1000000)
def dfs(node):
 nonlocal l,vis
 st=True
 for i in adj[node]:
  if i in l:
   vis[a]+=it[i]
   st=False
   l.remove(i)
   dfs(i)
 if st:
  return ''
 
for _ in range(t):
 n,m,k=list(map(int,input().split()))
 adj=[[] for i in range(n)]
 l=set(range(0,n))
 for i in range(m):
  x,y=list(map(int,input().split()))
  adj[x-1].append(y-1)
  adj[y-1].append(x-1)
 it=list(map(int,input().split()))
 vis={}
 cost=[]
 while l!=set():
  a=l.pop()
  vis[a]=it[a]
  dfs(a)
  cost.append(vis[a])
 cost.sort()
 if len(cost)<k:
  print(-1)
  continue
 mi=0
 ma=len(cost)
 su=0
 for i in range(k):
  if i%2==0:
   su+=cost[ma-1]
   ma-=1
  else:
   su+=cost[mi]
   mi+=1
 print(su)





  
 

