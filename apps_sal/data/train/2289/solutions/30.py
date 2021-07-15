from copy import copy
from collections import deque
import sys
A = input()
N = len(A)
M = 26

def alp(c):
  return chr(ord("a")+c)
def num(s):
  return ord(s)-ord("a")
  

INF = 10**6
tmp = [INF for _ in range(M)]
Nxt = [None for _ in range(N+1)]
Nxt[N] = copy(tmp)
for i in range(N-1,-1,-1):
  tmp[num(A[i])] = i+1
  Nxt[i] = copy(tmp)
#print(*Nxt, sep = "\n")  
task = deque([(0, "")])
visited = {0}
  
while task:
  i, s = task.popleft()
  for c, j in enumerate(Nxt[i]):
    if j == INF:
      print("".join([s,alp(c)]))
      return
    if j not in visited:
      task.append((j, "".join([s,alp(c)])))
      visited.add(j)
    
print("error")
