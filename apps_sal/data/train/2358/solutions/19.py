from heapq import heapify,heappop,heappush
import sys
import math

input = sys.stdin.readline

xs, ys, xt, yt = list(map(int, input().split()))
N = int(input())

A = [(xs,ys,0)]
for i in range(N):
  A.append(tuple(map(int, input().split()))) # x, y, r = map(int, input().split())
A.append((xt,yt,0)) 

task = [[0.,0]]
heapify(task)
visited = set()
while task:
  #print(task)
  while task:
    c, p = heappop(task)
    if p not in visited:
      break
    if not task:
      print("error")
      return
  if p == N+1:
    print(c)
    return
     
  visited.add(p)
  xp, yp, rp = A[p] 
  
  for q in range(N+2):
    if q not in visited:
      xq, yq, rq = A[q]
      l = max(0.,math.sqrt((xq - xp)**2 + (yq - yp)**2)-rq-rp)
      heappush(task,[c+l, q])
  
  
    
    
      
  
  

