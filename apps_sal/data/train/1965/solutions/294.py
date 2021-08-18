class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(x):
            if x != father[x]:
                father[x] = find(father[x])
            return father[x]

        def union(x, y):
            fx, fy = find(x), find(y)
            if fx != fy:
                father[fy] = fx

        father = list(range(n + 1))
        r = g = 0
        res = 0
        for t, u, v in edges:
            if t == 3:
                if find(u) != find(v):
                    union(u, v)
                    r += 1
                    g += 1
                else:
                    res += 1

        father0 = father[:]
        for t, u, v in edges:
            if t == 1:
                if find(u) != find(v):
                    union(u, v)
                    r += 1
                else:
                    res += 1

        father = father0
        for t, u, v in edges:
            if t == 2:
                if find(u) != find(v):
                    union(u, v)
                    g += 1
                else:
                    res += 1
        return res if r == g == n - 1 else -1
