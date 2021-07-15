t=int(input())
while t!=0:
 n=int(input())
 a=list(map(int,input().split()))
 c=0
 for i in range(n-1):
  if (a[i]&1)!=1 :
   for j in range(i,n):
    if (a[j]&1)==1:
     c+=1
 print(c)
 t-=1

