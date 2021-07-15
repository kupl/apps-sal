import sys
import math
r=int(input())
for v in range (0,r):
 n = int(input())
 x=1
 arr=list(map(int,input().strip().split(" ")))
 for i in range (0,n):
  x=x*arr[i]
  
 for i in range (2,100000000):
  if(x%(pow(i,2))==0):
   ans1=i
   break
 
 
 print(ans1) 

