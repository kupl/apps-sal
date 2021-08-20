class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(x, y):
            (x, y) = (find(x), find(y))
            if x == y:
                return 0
            parent[x] = y
            return 1
        parent = list(range(n + 1))
        e1 = e2 = res = 0
        for (t, u, v) in edges:
            if t == 3:
                if union(u, v):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        parenttemp = parent[:]
        for (t, u, v) in edges:
            if t == 1:
                if union(u, v):
                    e1 += 1
                else:
                    res += 1
        if e1 != n - 1:
            return -1
        parent = parenttemp
        for (t, u, v) in edges:
            if t == 2:
                if union(u, v):
                    e2 += 1
                else:
                    res += 1
        if e2 != n - 1:
            return -1
        return res
