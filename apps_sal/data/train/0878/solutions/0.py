# cook your dish here

import numpy as np
 

def minstairs(n,k):
 stairsHeight=[]
 stairs=0
 current = 0
 stairsHeight=list(map(int, input().split()))
 stairsHeight=np.array(stairsHeight)
 curr=0
 for i in range(n):
  if stairsHeight[i]-curr<=k:
   curr=stairsHeight[i]
  else:
   if (stairsHeight[i]-curr)%k==0:
    stairs+=((stairsHeight[i]-curr)//k)-1
   else:
    stairs+=(stairsHeight[i]-curr)//k
   curr=stairsHeight[i]
 return stairs
  
T=int(input())
for i in range(T):
 n,k =list(map(int,input().split()))
 print(minstairs(n,k))

