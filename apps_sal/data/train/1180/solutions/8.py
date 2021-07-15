def res(x,y,n,k):
 d=abs(x-y)
 if x==y:
  return n,n
 elif x>y:
  if k%4==0:
   return d,0
  if k%4==1:
   return n,n-d
  if k%4==2:
   return n-d,n
  if k%4==3:
   return 0,d
 elif x<y:
  if k%4==0:
   return 0,d
  if k%4==1:
   return n-d,n
  if k%4==2:
   return n,n-d
  if k%4==3:
   return d,0
n=int(input())
for i in range(n):
 n,k,x,y=list(map(int,input().split()))
 a,b=res(x,y,n,k)
 print(a,b) 
 

