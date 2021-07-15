import math
t=int(input())
for _ in range(t):
 n=int(input())
 d=n*(n+1)/4
 if n*(n+1)%4!=0:
  print("0")
 else:
  x=math.floor((-1+(math.sqrt(1+8*d)))//2)
  if x*(x+1)/2==3:
   print("2")
  elif x*(x+1)/2==d:
   print(n-x) + sum(range(x)) + sum(range(n-x))
  else:
   print(n-x)
