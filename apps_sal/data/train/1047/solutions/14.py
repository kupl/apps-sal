t=int(input())
for i in range(t):
 n=int(input())
 x=[]
 y=[]
 dx=[]
 dy=[]
 for j in range(n):
  c=list(map(int,input().split()))
  x.append(c[0]-c[1])
  y.append(c[0]+c[1])
 x.sort()
 y.sort()
 for j in range(1,n):
  dx.append(x[j]-x[j-1])
  dy.append(y[j]-y[j-1])
 a=min(dx)
 b=min(dy)
 print('{0:.6f}'.format(min(a,b)/2))
