class UnionFind:
\t# uf = UnionFind(N)
\t# for i in range(N): uf.add(i)
\t# for x, y in pairs: uf.unite(x, y)
\t# ans = max([uf.size(i) for i in range(N)])
\tdef __init__(self, n):
\t\tself.n = n
\t\tself.sizes = [1]*n
\t\tself.parents = list(range(n))

\tdef find(self, x):
\t\twhile x != self.parents[x]:
\t\t\tself.parents[x] = self.parents[self.parents[x]]
\t\t\tx = self.parents[x]
\t\treturn self.parents[x]

\tdef unite(self, x, y):
\t\tx, y = self.find(x), self.find(y)
\t\tif x == y:
\t\t\treturn
\t\tif self.sizes[x] < self.sizes[y]:
\t\t\tx, y = y, x
\t\tself.parents[y] = x
\t\tself.sizes[x] += self.sizes[y]
\t
\tdef add(self, x):
\t\tself.sizes[x] = 1
\t\t
\tdef size(self, x):
\t\treturn self.sizes[self.find(x)]
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dists = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1, p2 = points[i], points[j]
                d = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                dists.append((d, i, j))
        dists.sort()
        uf = UnionFind(len(points))
        ans = 0
        for d, i, j in dists:
            if uf.find(i) != uf.find(j):
                #print(i, j, d)
                uf.unite(i, j)
                ans += d
        return ans
