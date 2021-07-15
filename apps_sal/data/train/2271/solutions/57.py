n,m=map(int,input().split())
P=[int(i) for i in input().split()]

uf=[i for i in range(n+1)]
def ufuf(x):
    while x!=uf[x]:
        x=uf[x]
    return x

for i in range(m):
    x,y=map(int,input().split())
    if ufuf(x)<ufuf(y):
        uf[ufuf(y)]=ufuf(x)
    else:
        uf[ufuf(x)]=ufuf(y)

ans=0
for i in range(1,n+1):
    if ufuf(i)==ufuf(P[i-1]):
        ans+=1
print(ans)
