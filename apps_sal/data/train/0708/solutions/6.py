mod=int(1e9+7)
for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 p=0
 for i in range(1,n+1):
  l=pow(k,2*i-1,mod)
  p=(p+l)%mod 
  k=(k*l)%mod 
 print(p)

