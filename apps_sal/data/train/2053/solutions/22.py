n,m = map(int,input().split())

b=list(map(int,input().split()))
g=list(map(int,input().split()))

b.sort()
g.sort()

if g[0]<b[n-1]:print(-1)
elif g[0]==b[n-1]:print(m*(sum(b)-b[n-1])+sum(g))
else:print(m*(sum(b)-b[n-1])+sum(g)+b[n-1]-b[n-2])
