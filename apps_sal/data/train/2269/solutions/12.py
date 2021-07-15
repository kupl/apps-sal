import sys
input = sys.stdin.readline
from itertools import combinations
n,m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]
g2d = [[1 for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
  g2d[i][i] = 0
for a,b in ab:
  g2d[a][b] = 0
  g2d[b][a] = 0
graph = [[] for i in range(n+1)]
for i in range(1,n+1):
  for j in range(1,n+1):
    if g2d[i][j]:
      graph[i].append(j)
      graph[j].append(i)
vis = [-1]*(n+1)
oddeven = []
for i in range(1,n+1):
  if vis[i] == -1:
    stack = [i]
    vis[i] = 0
    odd = 0
    even = 1
    while stack:
      x = stack.pop()
      for y in graph[x]:
        if vis[y] == -1:
          vis[y] = vis[x]+1
          if vis[y]%2:
            odd += 1
          else:
            even += 1
          stack.append(y)
        elif (vis[y]-vis[x])%2 == 0:
          print(-1)
          return
    oddeven.append(abs(odd-even))
t = len(oddeven)
s = sum(oddeven)
dp = 1<<s
for x in oddeven:
  dp = (dp<<abs(x)) | (dp>>abs(x))
for i in range(s+1):
  if (dp&1<<(s-i))|(dp&1<<(s+i)):
    ex = i
    break
A,B = (n+ex)//2,(n-ex)//2
print(A*(A-1)//2+B*(B-1)//2)
