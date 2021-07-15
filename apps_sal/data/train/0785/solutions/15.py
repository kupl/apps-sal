t=int(input())
while(t>0):
 n=int(input())
 b=bin(n)
 l=len(b)-2
 if(b.count('1')==1):
  l-=1
 x=1
 s=0
 for i in range(36):
  s+=n
  s-=x
  if(s<0):
   break
  x*=2
 print(i,l)
 t-=1
