# EXNETWRK.py

t = int(input())
for _ in range(t):
 n,m = list(map(int, input().split()))
 if n == m :
  for i in range(1,n+1):
   print(i,i%n+1)
 else:
  print(-1,-1)

