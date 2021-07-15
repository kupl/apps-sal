from sys import stdin,stdout




total_cost=0
def find(a):
 if par[a]==a:
  return a
 else:
  par[a]=find(par[a])
  return par[a]
def union(a,b,c):
 a,b=find(a),find(b)
 nonlocal total_cost
 total_cost+=(rank[a]*rank[b]*c)
 if a!=b:
  if rank[a]>rank[b]:
   par[b]=a
   rank[a]+=rank[b]
  elif rank[b]>rank[a]:
   par[a]=b
   rank[b]+=rank[a]
  else:
   par[a]=b;
   rank[b]+=rank[a]

n=int(stdin.readline().strip())
par=[i for i in range(n)]
rank=[1 for i in range(n)]
edges=[]
for i in range(n-1):
 u,v,c=stdin.readline().strip().split(' ')
 u,v,c=int(u)-1,int(v)-1,int(c)
 edges.append((c,u,v))
edges.sort()
tw=0
for i in edges:
 union(i[1],i[2],i[0])
 tw+=i[0]

stdout.write(str(tw-(total_cost/((n*(n-1))/2))))
