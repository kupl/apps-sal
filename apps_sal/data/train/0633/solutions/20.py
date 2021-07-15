for t in range(int(input())):
 n=int(input())
 x=int(input())
 for i in range(n-1):
  y=int(input())
  if y>x:
   x=y
 print(x)
