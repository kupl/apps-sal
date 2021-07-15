t=int(input())
while(t):
 t=t-1
 x,r,a,b=input().split()
 x=int(x)
 r=int(r)
 a=int(a)
 b=int(b)
 
 le=3.1415926*2*r*x
 rel=abs(a-b)
 m=le/rel
 hr=le/max(a,b)
 hr=hr*x
 print(int(hr/m-0.0001))
