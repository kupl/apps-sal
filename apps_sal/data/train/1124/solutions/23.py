for _ in range(int(input())):
 n,p,q=map(int,input().split())
 l=list(map(int,input().split()))
 l.sort()
 ans=0
 for i in range(n):
  x=l[i]//2
  if(q>0):
   if(q>=x and q>0):
    q-=x
    l[i]-=x*2
   else:
    l[i]-=q*2
    q=0
    x=0
  p-=l[i]
  if(p<0 and q<=0):
   break
  ans+=1
 print(ans)
