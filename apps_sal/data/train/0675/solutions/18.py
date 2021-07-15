import math
for x in range(int(input())):
 N=int(input())
 l=6
 m=3
 a=2**m
 if (N!=1 and math.ceil(math.log(N,2)))==math.floor(math.log(N,2)):
  print('-1')
  continue
 elif N==1:
  print('1')
 elif(N==3):
  print("2 3 1")
 elif(N==5):
  print("2 3 1 5 4")
 if(N>5):
  print("2 3 1 5 4",end=" ")
  while(l<=N):
   if(l==a):
    m=m+1 
    a=2**m
    print(l+1,end=" ")
    print(l,end=" ")
    l=l+2
   else:
    print(l,end=" ")
    l=l+1
   print(' ')
  



