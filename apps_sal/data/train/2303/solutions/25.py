from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M=list(map(int,input().split()))
if M==0:
  print((-1))
  return
G=defaultdict(set)
for i in range(M):
  a,b,c=list(map(int,input().split()))
  G[a+(c<<30)].add(b+(c<<30))
  G[b+(c<<30)].add(a+(c<<30))
  G[a].add(a+(c<<30))
  G[b].add(b+(c<<30))
  G[a+(c<<30)].add(a)
  G[b+(c<<30)].add(b)
def BFS(x):
  d={}
  for k in list(G.keys()):
    d[k]=float("inf")
  stack=deque([(x,0)])
  if x not in d:
    return -1
  while stack:
    s,m=stack.popleft()
    if s==N:
      return m
    if d[s]>m:
      d[s]=m
      if s>=(1<<30):
        for i in G[s]:
          if d[i]>10**30:
            stack.appendleft((i,m))
      else: 
        for i in G[s]:
          if d[i]>10**30:
            stack.append((i,m+1))
  return -1

print((BFS(1)))



      
    

