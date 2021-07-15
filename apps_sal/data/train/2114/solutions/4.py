n, m=list(map(int, input().split()))
ans=0
f=list(map(int, input().split()))
for i in range(m):
    a, b, x=list(map(int, input().split()))
    ans=max(ans, (f[a-1]+f[b-1])/x)
print(ans)

