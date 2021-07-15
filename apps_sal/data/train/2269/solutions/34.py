n,m,*A=map(int,open(0).read().split())
g=[[1]*n for _ in [0]*n]
for a,b in zip(A[::2],A[1::2]):
    g[a-1][b-1]=g[b-1][a-1]=0
U=[1]*n
D=1
def dfs(v):
    nonlocal D
    R[U[v]]+=1
    for k in range(n):
        if g[v][k]*(k-v):
            D *= U[k]!=U[v]
            if U[k]>0:
                U[k]=~U[v]
                dfs(k)
for i in range(n):
    if U[i]>0:
        R=[0,0];U[i]=0
        dfs(i);
        D=(D<<R[0])|(D<<R[1])
a=-1
for i in range(n//2+1):
    if D>>i&1:a=(i*(i-1)+(n-i)*(n-i-1))//2
print(a)
