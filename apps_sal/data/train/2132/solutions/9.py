import  sys
input=sys.stdin.readline
#sys.setrecursionlimit(1000000)

n=int(input())
fr=[0]*(n+2)
fr[0]=1
d=[0]*(n+2)
mod=int(998244353)

for i in range(1,n+1):
    fr[i]=(fr[i-1]*i)%mod

for i in  range(n-1):
    u,v=map(int,input().split())
    d[u]+=1;d[v]+=1

ans=n

for i in range(1,n+1):
    ans=ans*fr[d[i]]
    ans%=mod

print(ans)
