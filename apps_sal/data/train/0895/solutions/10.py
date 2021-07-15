n=int(input())
l=list(map(int,input().split()))
d=l.copy()
for i in range(2,n):
    mini=min(d[i-1],d[i-2])
    d[i]+=mini
f=l.copy()
f=f[::-1]
for i in range(2,n):
    mini=min(f[i-1],f[i-2])
    f[i]+=mini
print(min(f[-1],d[-1]))
