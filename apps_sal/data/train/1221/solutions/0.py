from math import sqrt

T = int(input())
ans = []

for _ in range(T):
 X = int(input())

 count = 0
 x = 0
 y = 0
 while(x<=X):
  p = int(sqrt(y))
  count += 1
  if(p*p>y):
   x = p
   y += p**2
  else:
   x = p+1
   y += (p+1)**2
 if(x<=X):
  ans.append(count)
 else:
  ans.append(count-1)

for i in ans:
 print(i)
