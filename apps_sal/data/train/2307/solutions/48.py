N,A,B=map(int,input().split())
X=list(map(int,input().split()))
ans=0
for i in range(1,N):
    if A*(X[i]-X[i-1])>=B:
        ans+=B
    else:
        ans+=A*(X[i]-X[i-1])
print(ans)
