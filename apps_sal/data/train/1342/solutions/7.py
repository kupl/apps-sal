for _ in range(int(input())):
 n,x= map(int,input().split())
 l=list(map(int,input().split()))
 l.sort()
 i=0
 count=0
 while(i<n):
  if l[i]<=x:
   count+=1
   x=max(l[i]*2,x)
   i+=1
  elif l[i]>x:
   count+=1
   x=x*2
 print(count)
