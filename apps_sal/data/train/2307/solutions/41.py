n,a,b=list(map(int,input().split()))
x=list(map(int,input().split()))
ans=0
for i in range(n-1):
    costa=(x[i+1]-x[i])*a
    ans+=min(b,costa)
print(ans)

