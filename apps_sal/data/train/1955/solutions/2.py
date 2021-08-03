class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))
        self.rank = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.par[px] = py
        elif self.rank[px] > self.rank[py]:
            self.par[py] = px
        else:
            self.par[py] = px
            self.rank[px] += 1


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        uf = UnionFind(N)
        res = [''] * N
        indices = defaultdict(list)

        for u, v in pairs:
            uf.union(u, v)

        for i in range(N):
            indices[uf.find(i)].append(i)

        for i in indices:
            chars = sorted([s[j] for j in indices[i]])
            for j in range(len(indices[i])):
                res[indices[i][j]] = chars[j]

        return ''.join(res)
