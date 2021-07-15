for ii in range(eval(input())):
 n,m=list(map(int,input().split()))
 arr=list(map(int,input().split()))
 import math
 su=0
 for i in range(m):
  su=su+arr[i]
 k=su
 nextsum=0
 for iI in range(m,n):
  nextsum=nextsum+(math.ceil(arr[iI]/2))
 l=nextsum
 if (k-l)>=0:
  print("VICTORY")
 else:
  print("DEFEAT")

