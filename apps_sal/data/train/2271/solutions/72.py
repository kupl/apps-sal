class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def find_root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
        
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
                
    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.root[self.find_root(x)]

    
f=lambda:map(int,input().split())
N,M=f()
uf=UnionFind(N+1)

p=list(f())
p_index=[[] for _ in [0]*(N+1)]
for i in range(1,N+1):
    p_index[p[i-1]]=i
for _ in [0]*M:
    uf.unite(*f())


index_list=[[] for _ in [0]*(N+1)]
group_list=[[] for _ in [0]*(N+1)]

for i in range(1,N+1):
    index_list[uf.find_root(i)].append(p_index[i])
    group_list[uf.find_root(i)].append(i)
    
res=0
for i in range(1,N+1):
    if i==uf.find_root(i):
        res+=len(set(index_list[i]) & set(group_list[i]))

print(res)
