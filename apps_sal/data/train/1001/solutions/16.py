t=int(input())
while(t>0):
 n=int(input())
 l=list(map(int,input().split()))
 c=1
 x=l[0]
 for i in range(1,n):
  if(x==l[max(i-6,0)]):
   x=min(l[max(0,i-5):i])
  else:
   x=min(l[i-1],x)
  if(l[i]<x):
   c+=1
 print(c)
 t-=1
