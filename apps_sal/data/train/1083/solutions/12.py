import sys
import math
t=int(eval(input("")))
while t:
 n,m,z,l,r,b=list(map(int,sys.stdin.readline().split()))
 if m==3:
  if n==1:
   if z+l+r+b<3:
    print(z+l+r+b)
   else:
    if b<2 :
     print(3)
    elif b==2 and z<1 and l+r<2:
     print(2)
    elif b==3 and z<1 and l+r<2:
     print(2)
    else:
     print(3)
  elif n==2:
   if z+l+r+b<6:
    print(z+l+r+b)
   elif z!=0:
    print(6)
   elif z==0 and b==3 and z+l+r+b==6:
    print(5)
   else:
    print(6)
  elif n==3:
   if z+l+r+b<9:
    print(z+l+r+b)
   else:
    print(9)
   
    
 elif m==2:
  if n==1:
   if z+l+r+b<2:
    print(z+l+r+b)
   elif l+r+z==0:
    print(1)
   else:
    print(2)
  elif n==2:
   if z+l+r+b<4:
    if z+l+r+b<3:
     print(z+l+r+b)
    elif b==3 and z+l+r==0:
     print(2)
    else:
     print(3)
   elif z+l+r>1:
    print(4)
   else:
    print(3)
  elif n==3:
   if z+l+r+b<6:
    print(z+l+r+b)
   else:
    print(6)
   
 else:
  print(min(m*n,z+l+r+b))
  
 t-=1

