# cook your dish here
from collections import Counter
from math import factorial
for _ in range(int(input())):
 
 s=input()
 c=Counter(s)
 k=factorial(len(s))
 
 for value in list(c.values()):
  
  if value>1:
   k=k//factorial(value)
   
 print(k%(10**9+7))
 
 
 

