import math
t=int(input())
while(t >=1):
 n=int(input())
 l=6
 m=3
 a = 2**m

 if(n!=1 and math.ceil(math.log(n,2)) == math.floor(math.log(n,2))):
  print("-1")
  t=t-1
  continue
 if(n==1):
  print("1",end=" ")
 elif(n==3):
  print("2 3 1",end=" ")
 elif(n==5):
  print("2 3 1 5 4",end=" ")
 if(n>5):
  print("2 3 1 5 4",end=" ")
  while(l<=n):
   if(l==a):
    m=m+1 
    a=2**m
    print(l+1,end=" ")
    print(l,end=" ")
    l=l+2
   else:
    print(l,end=" ")
    l=l+1
 if(t>=2):
  print()
 t=t-1


  
