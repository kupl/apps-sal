# cook your dish here
for j in range(int(input())):
 n=int(input())
 x=list(map(int,input().split()))
 w=x.copy()
 t=x.copy()
 d=x[1]-x[0]
 z=[x[0],x[1]]
 for i in range(2,n):
  x[i]=x[i-1]+d
  z.append(x[i])
 e=t[-1]-t[-2]
 y=[t[-1],t[-2]]
 for i in range(n-2):
  t[n-2-i-1]=t[n-2-i]-e
  y.append(t[n-2-i-1])
 y.reverse()
 am,bm=0,0
 for i in range(n):
  if(w[i]!=y[i]):
   am+=1
   if(am>1):
    break
  if(w[i]!=z[i]):
   bm+=1
   if(bm>1):
    break
 if(am==1):
  print(*y)
 else:
  print(*z)

