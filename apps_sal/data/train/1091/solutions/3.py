import math
t = int(input())
for _ in range(0,t):
 n = int(input())
 #print(n)
 sides = []
 for i in range(2,(n+n)):
  if i % 2 == 0 and i != n:
   sides.append(i//2)
 f = 0
 for i in sides:
  pyt = (n*n - i*i)
  if math.sqrt(pyt) - int(math.sqrt(pyt)) == 0.000000:
   print("YES")
   f = 1
   break
 if f == 0:
  print("NO")

