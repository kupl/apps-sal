n,a,b=map(int,input().split())
A=list(map(int,input().split()))
ans=0
for i in range(n-1):
    if (A[i+1]-A[i])*a < b:
        ans+=a*(A[i+1]-A[i])
    else:
        ans+=b
print(ans)
