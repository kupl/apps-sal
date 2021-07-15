n,m= map(int,input().split())
par = [-1]*(n)
def find(x):
    if par[x]<0:return x
    else:
        par[x]=find(par[x])
        return par[x]
def unite(x,y):
    px,py=find(x),find(y)
    if px==py:return False
    else:
        if px<py:px,py=py,px
        par[px]+=par[py]
        par[py]=px
        return True
p= list(map(int,input().split()))
gl=[[] for _ in range(n)]
for i in range(m):
    x,y= map(int,input().split())
    unite(x-1,y-1)
for c in range(n):#par:
    ap=find(c)
    gl[ap].append(c)
g=0
for sg in gl:
    temp=[p[index]-1 for index in sg]
    newset = set(sg) & set(temp)
    g+=len(newset)
print(g)
