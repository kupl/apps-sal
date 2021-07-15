# cook your dish here
t=int(input())
import math
while t:
 t=t-1
 n,k=input().split()
 n=int(n)
 k=int(k)
 l=[-1*(i+1) for i in range(n)]
 for i in range(1,n,2):
  l[i]=l[i]*(-1)
 #print(l)
 if k-(math.floor(n/2))>0:
  s=k-(math.floor(n/2))
  while s:
   for i in range(n-1,-1,-1):
    # print(i,s,"*",l)
    if l[i]<0:
     l[i]=(-1)*l[i]
     s=s-1
     break
 if (math.floor(n/2))-k>0:
  s=(math.floor(n/2))-k
  while s:
   for i in range(n-1,-1,-1):
    if l[i]>0:
     l[i]=(-1)*l[i]
     s=s-1
     break
 for i in range(n):
  print(l[i],end=" ")
