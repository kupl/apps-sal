N,M=map(int,input().split())
*P,=map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(M)]

R=[-1]*(N+1)
def root(x):
    while R[x]>=0:
        x=R[x]
    return x
def union(x,y):
    x=root(x)
    y=root(y)
    if x==y:
        return
    if R[x]>R[y]:
        x,y=y,x
    R[x]+=R[y]
    R[y]=x

for x,y in xy:
    union(x,y)
ans=sum(root(i+1)==root(P[i])for i in range(N))
print(ans)
