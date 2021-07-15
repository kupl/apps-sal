test=int(input())
for i in range(0,test):
 n,k=list(map(int,input().split()))
 l=str(k)*n
 l=int(l)
 k=l*l
 u=str(k).strip()
 t=len(u)
 j=1
 ans=0
 for h in range(0,t):
  ans = ans+((int(u[h])%1000000007)*(j%1000000007)%1000000007)%1000000007
  j=(23*j)%1000000007
 print(ans%1000000007)
