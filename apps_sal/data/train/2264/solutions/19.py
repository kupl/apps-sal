from heapq import*
def f(s):
 a=[1<<50]*N;a[s]=0;p=[(0,s)];c=[0]*N;c[s]=1
 while p:
  d,v=heappop(p)
  if d<=a[v]:
   for u,w in G[v]:
    if a[u]>d+w:a[u]=d+w;heappush(p,(d+w,u));c[u]=0
    c[u]+=c[v]*(a[u]==d+w)
 return a,c
n=lambda:map(int,input().split());N,M=n();N+=1;S,T=n();G=[[]for _ in[0]*N]
for _ in[0]*M:U,V,D=n();G[U]+=(V,D),;G[V]+=(U,D),
P,X=f(S);Q,Y=f(T);s=P[T];print((X[T]**2-sum(-~s%2*x*x*y*y*(p==q==s//2)+(p<q)*x*x*sum((p+d+Q[j]==s)*(Q[j]<P[j])*Y[j]**2for j,d in g)for g,p,q,x,y in zip(G,P,Q,X,Y)))%(10**9+7))
