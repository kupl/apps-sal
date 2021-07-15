for i in range(int(input())):
 s=input()
 r=input()
 n=len(r)
 gap=[]
 t=0
 l=0
 for i in range(0,n):
  if s[i]==r[i]:
   t+=1
  else:
   gap.append(t)
   l+=1 
   t=0

 gap.append(t) 
 gp=len(gap)-1
 gap=gap[1:-1]
 gap.sort()
 x=l*gp
 for i in range(len(gap)):
  gp-=1
  l+=gap[i]
  y=gp*l
  if y<x:
   x=y
 print(min(x,n)) 
 

