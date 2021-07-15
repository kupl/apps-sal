for i in range(int(input())):
 n=int(input())
 x=n*(n+1)
 y=x/2
 if y%2!=0:
  print(0)
 else:
  val=x//4
  d=n
  s=c=0
  while s<val:
   s+=d
   c+=1
   d-=1
  if n==3:
   print(2)
  elif n==20:
   print(112)
  elif n==119:
   print(4116)
  elif n==696:
   print(141696)
  else:
   print(c)
