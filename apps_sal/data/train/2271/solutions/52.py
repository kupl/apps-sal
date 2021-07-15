class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    def same(self, x, y):
        return self.find(x) == self.find(y)
n,m=map(int,input().split())
p=[0]+list(map(int,input().split()))
uf=UnionFind(n)
for _ in range(m):
  a,b=map(int,input().split())
  uf.unite(a,b)
cnt=0
for i,j in enumerate(p):
  if uf.same(i,j):cnt+=1
print(cnt-1)
