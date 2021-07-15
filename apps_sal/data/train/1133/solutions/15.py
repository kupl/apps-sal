# cook your dish here
import math
def find_gcd(x, y): 
 while(y): 
  x, y = y, x % y 
 
 return x 
t=int(input())
for i in range(0,t):
 n=int(input())
 l=list(map(int,input().split()))
 l.sort()
 x=len(l)
 if(x>2):
  num1=l[0] 
  num2=l[1] 
  gcd=find_gcd(num1,num2) 
  for i in range(2,len(l)): 
   gcd=find_gcd(gcd,l[i]) 
 elif(x==2):
  gcd=math.gcd(l[0],l[1])
 else:
  gcd=l[0]
 c=sum(l)//gcd
 print(gcd,c)
