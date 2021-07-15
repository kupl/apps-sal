
for _ in range(int(input())):

 n,x=list(map(int,input().split()))

 l=list(map(int,input().split()))

 l.sort()

 i=cnt=0
 while i<n and 2*l[i]<x:
  cnt+=1

  i+=1

 while i<n:
  cnt+=1
  
  if l[i]>x and 2*(l[i]-x)>l[i] :
   x=x*2
   continue

  if l[i]<=x:
   x=l[i]
   i+=1

  x=x*2

 print(cnt)

