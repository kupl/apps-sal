import math as m
def isprime(n):
 for i in range(2,int(m.sqrt(n))+1):
  if(n%i==0):
   return False
 return True

for _ in range(int(input())):
 x,y=map(int,input().split())
 z=(x+y)
 i=z
 while(True):
  if isprime(z+1):
   ans=z+1
   break
  else:
   z+=1
 print(ans-i)
