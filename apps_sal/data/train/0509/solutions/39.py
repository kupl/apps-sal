from collections import defaultdict
from collections import deque

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in list(self.all_group_members().items()))
      
      
      
n,m = list(map(int,input().split()))
V = [[] for i in range(n+1)]

sets = [set([]) for i in range(n+1)]
uf = UnionFind(n+1)
for i in range(m):
    a,b,c = list(map(int,input().split()))
    if uf.find(a) != uf.find(b):
        uf.union(a,b)
        V[a].append([b,c])
        V[b].append([a,c])
        sets[a].add(c)
        sets[b].add(c)
        
p = [-1]*(n+1)

def out_not_in_number(x):
    ret = -1
    for i in range(1,n+1):
        if i not in sets[x]:
            ret = i
            break
    return ret

start = 1
p[start] = out_not_in_number(start)

q = deque([])
q.append(start)
while q:
    x = q.popleft()
    for y,z in V[x]:
        if p[y] == -1:
            q.append(y)
            if p[x] == z:
                p[y] = out_not_in_number(y)
                
            else:
                p[y] = z
for i in range(1,n+1):
    print((p[i]))
#print(V)

