import math
t=int(input())
for i in range(t):
 n=int(input())
 m=[0]
 for i in range(n):
  s,p,v=map(int,input().split())
  m.append((p//(s+1))*v)
 print(max(m))
