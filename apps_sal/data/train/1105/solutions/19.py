# cook your dish here
for i in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 l.sort()
 len1=len(l)
 a=l[len1-1]
 b=l[len1-2]
 len1-=2
 sum=0
 c=0
 for j in range(n-1):
  if l[j]!=l[j+1]:
   c=1
 if c==0:
  if n%2!=0:
   n=(n//2)+1
   print(n*l[0])
  else:
   n=n//2
   print(n*l[0])
 else:
  while(len1>=0):
   if len1==0:
    z=max(a,b)
    sum+=z
    break
   else:
    z=min(a,b)
   sum+=z
   len1-=1
   if a<b:
    a=l[len1]
    b=b-z
   else:
    b=l[len1]
    a=a-z
  print(sum)
    
   
  

