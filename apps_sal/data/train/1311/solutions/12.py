# cook your dish here
import math
try:
 t=int(input())
 for _ in range (t):
  n,k=list(map(int,input().split()))
  seq=[]
  for i in range(1,n+1):
   if i%2!=0:
    seq.append(i)
   else:
    seq.append(-i)
  positive=math.ceil(n/2)
  if(positive>k):
   i=n-1
   req=positive-k
   while (req>0):
    if seq[i]>0:
     seq[i] =-(i+1)
     req -=1
    i -=1
  if(positive<k):
   i=n-1
   req=k-positive
   while (req>0):
    if seq[i]<0:
     seq[i] =(i+1)
     req -=1
    i -=1
  print(*seq)
except EOFError as t : pass
  

