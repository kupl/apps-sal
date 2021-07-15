# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 a = list(map(int, input().split()))
 b = list(map(int, input().split()))
 dist = 0
 x = 0
 y = 0
 for i in range(n):
  x = x + a[i]
  y = y + b[i]
  if a[i]==b[i] and x==y:
   dist = dist + a[i]
 print(dist)
