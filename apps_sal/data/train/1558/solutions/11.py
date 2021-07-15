for x in range(int(input())):
 n,m=map(int,input().split())
 y=n*m
 for x in range(n*m):
  a=1
  b=1
  d={(1,1):1}
  count=1
  if x==0:
   print(n*m,end=" ")
   continue
  while(True):
   b=b+x+1
   if(b>m):
    u=b-m
    if(u%m==0):
     a=a+u//m
     b=m
    else:
     a=a+(u//m)+1
     b=u%m
   if a>n:
    break
   else:
    d[(a,b)]=1
    count+=1
  a=1
  b=1
  while(True):
   a=a+x+1
   if(a>n):
    u=a-n
    if(u%n==0):
     b=b+u//n
     a=n
    else:
     b=b+(u//n)+1
     a=u%n
   if b>m:
    break
   else:
    if (a,b) not in d.keys():
     count+=1
  print(count,end=" ")
 print("")
  
   

