from fractions import gcd
from functools import reduce
a=eval(input())
while(a):

 x=eval(input())
 b=list(map(int,input().split()))
 print(reduce(gcd,(b))*x)
 
  


 a-=1

