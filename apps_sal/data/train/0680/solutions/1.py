# cook your dish here
import math
import re 
import os
import sys
input=sys.stdin.readline
for i in range(int(input())):
 a_s=0
 b_s=0
 M=998244353
 ans=0
 n,m=list(map(int,input().split()))
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 a_s=sum(a)
 b_s=sum(b)
 q=int(input())
 for i in range(0,q):
  I=list(map(int,input().split()))
  if(I[0]==3):
   ans=(a_s*b_s)%M 
   print(ans)
  else:
   t,l,r,x=list(map(int,I))
   if(t==1):
    a_s=(a_s+(x*(r-l+1)))%M 
   else:
    b_s=(b_s+(x*(r-l+1)))%M

