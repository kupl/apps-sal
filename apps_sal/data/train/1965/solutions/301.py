class Solution:

    def maxNumEdgesToRemove(self, N: int, edges: List[List[int]]) -> int:

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            (x, y) = (find(x), find(y))
            if x == y:
                return 0
            parent[x] = y
            return 1
        (res, e1, e2) = (0, 0, 0)
        parent = [x for x in range(N + 1)]
        for (t, x, y) in edges:
            if t == 3:
                if union(x, y):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        parent_ = parent[:]
        for (t, x, y) in edges:
            if t == 1:
                if union(x, y):
                    e1 += 1
                else:
                    res += 1
        parent = parent_
        for (t, x, y) in edges:
            if t == 2:
                if union(x, y):
                    e2 += 1
                else:
                    res += 1
        return res if e1 == N - 1 and e2 == N - 1 else -1
