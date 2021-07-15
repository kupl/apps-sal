import math
for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 m=int(input())
 b=list(map(int,input().split()))
 k=0
 for j in range(n):
  if (a[j] == b[k]):
   k+=1
   if(k==m):
    break
 print('Yes' if k==m else 'No')
