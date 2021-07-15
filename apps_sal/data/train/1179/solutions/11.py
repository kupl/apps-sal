from math import log2,ceil

n=int(input())
for i in range(n):
  m=int(input())
  if m%4==1 or m%4==2:
   print(0)
  else:
   s=m*(m+1)//2
   f=m
   res=0
   si=0
   sm=s//2 
   while True:
    si+=f
    t=si-sm
    if t>0:
     if t>=m:
       break
     res+=min([t,m-t,m-f+1,f-1])
    elif t==0:
     p1=f-1
     p2=m-f
     res+=(p1*(p1-1)+p2*(p2+1))//2
    f=f-1
   print(res)
   

