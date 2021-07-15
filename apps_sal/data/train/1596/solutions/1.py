import math
t=int(input())
for i in range(t):
 p,q=list(map(int,input().split()))
 c=0
 h=0
 while(p>=0):
  if(p==0):
   c+=1
   break
  
  else:
   d=int(math.log(p+1,2))
  
   if(d==0):
    c+=1
    break
   
   y=(2**d)-1
   p-=y+1
   if(p==-1):
    c+=1
    break
   c+=1
 while(q>=0):
  if(q==0):
   h+=1
   break
  
  d=int(math.log(q+1,2))
  if(d==0):
   h+=1
   break
  y=(2**d)-1
  q-=y+1
  if(q==-1):
   h+=1
   break
  h+=1
 if(c==h):
  print(0,0)
 else:
  if(c<h):
   print(1,h-c)
  else:
   print(2,c-h)
  
  
 
 
  
  
  
 

