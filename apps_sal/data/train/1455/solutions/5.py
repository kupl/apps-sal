N = eval(input())
import math
arr=list(map(int,input().split()))
M=eval(input())
for iI in range(M):
 L,R=list(map(int,input().split()))
 su=0
 ok = arr[L-1:R]
 #print ok
 aks=len(ok)
 ok.sort()
 for ii in range(0,aks-1):
  su=su+(math.pow((ok[ii+1]-ok[ii]),2))
 print(int(su)) 
 
 

