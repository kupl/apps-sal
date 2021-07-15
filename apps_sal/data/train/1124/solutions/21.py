for _ in range(int(input())):
 n,p,q=map(int,input().split())
 l=list(map(int,input().split()))
 l.sort()
 ans=0
 for i in range(n):
  x=min(q,l[i]//2)
  l[i]-=x*2
  if(l[i]<=p):
   p-=l[i]
   q-=x
   ans+=1
 print(ans)
