for i in range(int(input())):
 n,m= map(int,input().split())
 
 c=0
 c+= n//m
 p= n%m
 
 if(p>=1):
  if(p%2==0 or p==1):
   c+=1
   print(c)
  else:
   c+=2
   print(c)
 else:
  print(c)
