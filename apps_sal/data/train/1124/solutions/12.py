# cook your dish here
t=int(input())
while t>0:
 n,p,q=input().split(" ")
 n=int(n)
 p=int(p)
 q=int(q)
 l=list(map(int,input().split(" ")))
 if q==0:
  s=0
  count=0
  l.sort()
  for i in l:
   s=s+i
   if s>p:
    break
   else:
    count=count+1
  print(count)
 elif p==0:
  l1=list(filter(lambda x:x%2==0,l))
  s=0
  count=0
  l1.sort()
  for i in l1:
   s=s+i
   if s>2*q:
    break
   else:
    count=count+1
  print(count)
 else:
  sum=p+2*q
  s=0
  count=0
  for i in l:
   s=s+i
   if s>sum:
    break
   else:
    count=count+1
  print(count)
   
  
 t=t-1
