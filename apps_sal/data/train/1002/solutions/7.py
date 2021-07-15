t=int(input())
for _ in range(t):
 n,d=map(int,input().split())
 a=list(map(int,input().split()))
 v={i:0 for i in a}
 v[a[0]]=1
 x=a[0]
 poss=1
 poss2,poss3=True,True
 a.sort()
 for i in range(n-1):
  if(a[i+1]-a[i]>d):
   poss=0
   break
 if(poss):
  st=a.index(x)
  if st!=n-1 and st!=0 and poss:
   for i in range(st):
    if (a[i+2]-a[i])>d:
     poss2=False
     break
   if poss2==False:
    for i in range(st-1,n-2):
     if (a[i+2]-a[i])>d:
      poss3=False
      break
 if((poss2 or poss3) and poss):
  print("YES")
 else:
  print("NO")
