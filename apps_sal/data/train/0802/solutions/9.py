import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations

def li():
 return list(map(int , input().split()))

def num():
 return map(int , input().split())

def nu():
 return int(input())

def find_gcd(x , y):
 while (y):
  x , y = y , x % y
 return x

def ans(index,seta,setb,carry):
 if(seta<0 or setb<0):
  return 0
 if(index==inc):
  if(carry==0 and seta==0 and setb==0):
   return 1
  else:
   return 0
 if(dp[index][seta][setb][carry]!=-1):
  return dp[index][seta][setb][carry]
 z=int(sc[index])
 res=0
 if(carry==z):
  res+=ans(index+1,seta,setb,carry//2)
  res += ans(index + 1 , seta-1 , setb-1 , (2+carry)//2)
 if((1+carry)%2==z):
  res += ans(index + 1 , seta-1 , setb , (1+carry)//2)
  res += ans(index + 1 , seta , setb-1 , (1+carry)//2)
 dp[index][seta][setb][carry]=res
 return res

t=nu()
for it in range(t):
 a,b,c=num()
 sa=str(bin(a))[2:]
 sb=str(bin(b))[2:]
 zc=str(bin(c))[2:]
 ca=sa.count("1")+1
 cb=sb.count("1")+1
 cc=zc.count("1")+1
 inc=len(zc)
 sc=zc[::-1]
 dp=[-1]*inc
 for i in range(inc):
  dp[i]=[-1]*ca
  for j in range(ca):
   dp[i][j]=[-1]*cb
   for k in range(cb):
    dp[i][j][k]=[-1]*2
 print(ans(0,ca-1,cb-1,0))
