t=int(input())
while(t>0):
 n,k=map(int,input().split())
 l=list(map(int,input().split()))
 x=3*10**9
 c=0
 for i in range(n):
  for j in range(i+1,n):
   y=abs(l[j]+l[i]-k)
   if(y<x):
    x=y
 for i in range(n):
  for j in range(i+1,n):
   if(abs(l[j]+l[i]-k)==x):
    c+=1
 print(x,c)
 t-=1
