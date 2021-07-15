from functools import reduce
def GCD(a,b):
 
 a = abs(a)
 b = abs(b)
 while a:
   
  a, b = b%a, a
 return b
  
  
def GCD_List(list):
 
 
 return reduce(GCD, list)
a=eval(input())
while(a):

 x=eval(input())
 b=list(map(int,input().split()))
 print(GCD_List(b)*x)
 
 
  


 a-=1

