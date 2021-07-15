
from collections import Counter
def fn(a):
 c = Counter(a)
 single = []
 double = []
 for i in c.keys():
  if c[i]>2:
   return 0
  if c[i] == 2:
   double.append(i)
  single.append(i)
 single.sort()
 double.sort(reverse = True)
 try:
  if single[-1] == double[0]:
   return 0
 except:
  pass

 return single+double
 
for _ in range(int(input())):
 n = int(input())
 a = list(map(int,input().split()))
 g = fn(a)
 if g:
  print("YES")
  print(*g)
 else:
  print("NO")
