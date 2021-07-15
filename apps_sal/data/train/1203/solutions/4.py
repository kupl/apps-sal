mm=1000000007
def abc(a,b):
 c=1
 d=1
 for i in range(b):
  c=(c*a)%mm
  a-=1
  d=(d*(i+1))
 return (c*pow(d,mm-2,mm))%mm 
  
  

t=int(input())
while t>0:
 n,m=[int(x) for x in input().split()]
 while m>0:
  a,b=[int(x) for x in input().split()]
  if b>a:
   print(0)
  else:
   r=abc(a-1,b-1)
   print((r*pow(2,n-a,mm))%mm)
  m-=1
 t-=1 

