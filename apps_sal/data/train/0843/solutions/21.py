t=int(input())
while(t>0):
 l=[]
 n=int(input())
 for i in range(n):
  l.append(list(map(int,input().split())))
 x=max(l[-1])
 w=0
 s=x
 for i in range(n-2,-1,-1):
  l[i].sort(reverse=True)
  q=0
  for j in l[i]:
   if(j<x):
    x=j
    q=1
    s+=x
    break
  if(q==0):
   w=1
   print(-1)
   break
 if(w==0):
  print(s)
 t-=1
