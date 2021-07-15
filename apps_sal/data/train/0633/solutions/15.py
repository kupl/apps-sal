t = int(input())
for _ in range(t):
 n = int(input())
 H = -1
 for i in range(n):
  h = int(input())
  if h>H:
   H = h
 print(H)
