a=int(input())
for w in range(a):
 b=input()
 c=input()
 d=len(b)
 e=[]
 r=0
 t=0
 p=0
 i=0
 z=0
 y=1 
 for k in range(d):
  if(b[k]!=c[k]):
   r=r+1
   t=1
   if(i!=y):
    z=z+1
    y=0
   if(p>0):
    e.append(p)
    p=0 
  elif(t==1 and b[k]==c[k]):
   p=p+1
   y=1 
 e.sort()
 n=r*z
 j=len(e)
 for it in range(j):
  r=r+e[it]
  z=z-1
  if((r*z)<n):
   n=z*r
 print(n) 
