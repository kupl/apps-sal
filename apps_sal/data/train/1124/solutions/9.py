# cook your dish here
try:
 for _ in range(int(input())):
  n,p,q=list(map(int,input().split()))
  l=list(map(int,input().split()))
  l.sort()
  for i in range(n):
   a=l[i]//2
   q=q-a
   if(q>=0):
    l[i]=l[i]-(2*a)
   else:
    break
  i=0
  while(p>=0 and i<n):
   p=p-l[i]
   if(p>=0):
    l[i]=0
   i+=1
  print(l.count(0))
   
   
   
  
except:
 pass

