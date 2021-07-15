# cook your dish here
T = int(input())
for _ in range(T):
 n = int(input())
 arr = list(map(int, input().strip().split()))
 s = set()
 if n > 60:
  print("NO")
 else:
  for i in range(n):
   ordd = 0
   for j in range(i, n):
    ordd = ordd | arr[j]
    s.add(ordd)
  if len(s) == n*(n+1) / 2:
   print("YES")
  else:
   print("NO")

