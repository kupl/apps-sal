try:
 t=int(input())
 while t>0:
  [a,b]=[int(x) for x in input().split()]
  if a==1 and b==1:
   print(1)
   continue
  if a%2==0:
   o1=a//2
   e1=a//2
  else:
   o1=a//2+1
   e1=a//2
  
  if b%2==0:
   o2=b//2
   e2=b//2
  else:
   o2=b//2+1
   e2=b//2
   
  print(e1*e2+o1*o2)
  t-=1
except:
 pass
