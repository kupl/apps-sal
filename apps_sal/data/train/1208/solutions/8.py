from collections import Counter
import string
import math
import sys
def array_int():
 return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
 if number_of_variables==1:
  return int(sys.stdin.readline())
 if number_of_variables>=2:
  return list(map(int,sys.stdin.readline().split())) 
def makedict(var):
 return dict(Counter(var))
mod=1000000007
fact=[1]*1000001
c=1
for i in range(1,1000001):
 fact[i]=(fact[i-1]*c)%mod
 c+=1
prod=[1]*1000001
pro=1
for i in range(1,1000000+1):
 pro=((pro%mod)*fact[i])%mod
 prod[i]=pro 
for _ in range(vary(1)):
 n=vary(1)
 
 
 print(prod[n]%mod)
 


 


 




