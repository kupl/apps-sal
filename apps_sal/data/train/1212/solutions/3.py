import numpy as np
from math import floor
def getFactors(n):
 factors=[];

 for i in range(1, n + 1):
  if (n % i == 0 and (n/i)<27):
   factors.append(i)
 #print(factors)
 return factors

t=input()
t=int(t)
while(t>0):
 t-=1
 s=input()
 n=len(s)
 fact=getFactors(n)
 str=list(s)
 #print(fact)
 tot=0
 u, c = np.unique(str, return_counts=True)
 
 c[::-1].sort()
 #print(c)
 c_sum=c.sum()
 c_size=len(c)
 
 min=100000000
 #  print(length_c)
 for i in fact:
  tot=0
  k=floor(c_sum/i)
  #print(k)
  if(k<c_size):
   for j in range(k):
    if(c[j]-i>0):
     tot+=c[j]-i
   for j in range(k,c_size):
    tot+=c[j]
  #    print(tot)
  else:
   for j in c:
    if(j-i>0):
     tot+=j-i
  #    print(tot)
  if(tot<min):
   min=tot
  
#       print(min)

 print(min) 
