n,s=map(int,input().split())
a=sorted(list(map(int,input().split())))
ans=0
if s>=a[n//2]:
    for i in range(n//2,n):
        if a[i]>=s:
            break
        ans+=(s-a[i])
else:
    for i in range(n//2,-1,-1):
        if a[i]<=s:
            break
        ans+=(a[i]-s)
print(ans)
