test = int(input())

for _ in range(test):
 n = int(input())
 arr = list(map(int,input().split(" ")))
 se = set(arr)
 t = 0
 res = 0
 for i in se:
  c = 0
  j = 0
  while j<n:
   if arr[j] == i:
    pp = 0
    while(arr[j] == i):
      j += 1
      pp += 1
      if j >= n:
       break
    c += ((pp+1)//2)
   j += 1
  if c > t:
   t = c
   res = i
  if c == t:
   res = min(res,i)
 print(res)
