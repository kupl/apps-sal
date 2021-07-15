from math import *
T=int(input())
for i in range(T):
 N,K=[int(j) for j in input().split(" ")]
 A=list(map(int,input().split(" ")))
 Ao=[]
 Ae=[]
 for k in range(len(A)):
  if k%2==0:
   Ae.append(A[k])
  else:
   Ao.append(A[k]) 

 count1=0
 count2=0 
 if K==0:
  for r in range(len(A)):
   if r%2==0:      
    count1+=A[r]
   else:
    count2+=A[r] 
 else:
  for o in range(K):
   e=max(Ae)
   f=min(Ao)
   g=Ae.index(e)
   h=Ao.index(f)
   Ae[g]=f
   Ao[h]=e
  for p in range(len(Ae)):
   count1+=Ae[p]
  for w in range(len(Ao)):
   count2+=Ao[w] 
 if count2>count1:
  print("YES")
 else:
  print("NO")

