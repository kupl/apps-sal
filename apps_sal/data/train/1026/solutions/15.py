# cook your dish here
for _ in range(int(input())):
 l=list(map(int,input().split()))
 mod=10**9+7
 l.sort()
 ans=(l[0]%mod)*((l[1]-1)%mod)*((l[2]-2)%mod)
 print(ans%mod)
