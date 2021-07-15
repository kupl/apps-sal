import math
def divisors(n):
 arr = []
 for i in range(1,1+int(math.ceil(math.sqrt(n)))):
  if n%i == 0:
   arr.append(i)
   arr.append(n//i)
 arr = list(sorted(set(arr)))
 return arr
try:
 t = int(input())
 while t:
  t -= 1
  a,m = map(int, input().split())
  divs = divisors(m)
  ans = []
  for d in divs:
   q = (m//d-1)/a
   if q%1 == 0 and q>0:
    ans.append((int(d*q)))
  ans.sort()
  print(len(ans))
  for i in ans:
   print(i, end = ' ')
  print()
except:
 pass
