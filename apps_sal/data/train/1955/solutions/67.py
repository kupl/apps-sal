class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (xroot, yroot) = (self.find(x), self.find(y))
        if xroot != yroot:
            self.parent[yroot] = xroot


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
        ans = []
        m = collections.defaultdict(list)
        for (i, j) in pairs:
            dsu.union(i, j)
        for i in range(n):
            m[dsu.find(i)].append(s[i])
        for key in list(m.keys()):
            m[key].sort(reverse=True)
        for i in range(n):
            ans.append(m[dsu.find(i)].pop())
        return ''.join(ans)
