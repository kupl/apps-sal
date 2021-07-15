class UnionFind:
  def __init__(self, N):
    self.par=[i for i in range(N)]
    self.rank=[0 for _ in range(N)]
    self.size=[1 for _ in range(N)]
    
  def unite(self, x, y):
    x=self.getroot(x)
    y=self.getroot(y)
    if x!=y:
      if self.rank[x]<self.rank[y]:
        x, y=y, x
      if self.rank[x]==self.rank[y]:
        self.rank[x]+=1
      self.par[y]=x
      self.size[x]+=self.size[y]
      
  def united(self, x, y):
    return self.getroot(x)==self.getroot(y)
      
  def getroot(self, x):
    if self.par[x]==x:
      return x
    else:
      self.par[x]=self.getroot(self.par[x])
      return self.par[x]

  def getsize(self, x):
    return self.size[self.getroot(x)]
  

N, M=map(int, input().split())
UF=UnionFind(N+1)
p=[0]+list(map(int, input().split()))
for _ in range(M):
  x, y=map(int, input().split())
  UF.unite(x, y)
  
print(sum([1 for i in range(1, N+1) if UF.getroot(i)==UF.getroot(p[i])]))
