import numpy as np
t = int(input())
for t in range(0,t):
 q= list(map (int, input().rstrip().split()))
 r=q[0]
 c=q[1]
 sum=0
 a = np.array([[int(x) for x in input().split()] for i in range(r)]) 
 if(a[0][0]<2 and a[0][c-1]<2 and a[r-1][0]<2 and a[r-1][c-1]<2):
  sum+=4
 for j in range(1,c-1):
  if(a[0][j]<3 and a[r-1][j]<3):
   sum=sum+2
   
 for i in range(1,r-1):
  if(a[i][0]<3 and a[i][c-1]<3):
   sum=sum+2
 for j in range(1,r-1):
  for i in range(1,c-1):
   if(a[j][i]<4):
    sum=sum+1
 if(sum==r*c):
  print("Stable")
 else:
  print("Unstable")
   
   
   

