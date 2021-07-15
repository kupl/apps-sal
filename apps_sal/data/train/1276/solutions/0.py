from bisect import *
for x in range(eval(input())):
 n,k = list(map(int,input().split()))
 arr = list(map(int,input().split()))
 arr.sort()
 t = 1
 result = 0
 y = 0
 while y < n:
  if arr[y]<t:
   y += 1
  elif arr[y]==t:
   t = t*2
   y += 1
  else:
   result += 1
   t = t*2
 
 while t < 2**(k):
  result += 1
  t = t*2
 print(result)
