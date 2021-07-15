t=int(input())
for x in range(t):
 n = int(input())
 lst1 = list(map(int,input().split()))
 c = 1
 m = lst1[0]
 for y in range(1,n):
  if lst1[y] <= m:
   c += 1
   m = lst1[y]
 print(c)
