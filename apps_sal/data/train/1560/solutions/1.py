import math

def nCr(n,r):
 f = math.factorial
 return f(n) / f(r) / f(n-r)


t = int(input())

for i in range(0,t):
 a = input().split()
 n = int(a[0])
 k = int(a[1])

 arr = input().split()

 arr = [int(x) for x in arr]

 count = 0

 for j in arr:
  if j == 0:
   count = count + 1

 ways = 0


 if(count == 0):
  if(k%2 == 0):
   l=0
   while l<=min(n,k):
    ways = ways + nCr(n,l)
    l = l+2

  else:
   l = 1
   while l<=min(n,k):
    ways = ways + nCr(n,l)
    l = l+2

  print(ways)

 else:
  n = n-count
  l = 0

  while l <= min(n,k):
   ways = ways + nCr(n,l)
   l = l+1

  print(ways)

