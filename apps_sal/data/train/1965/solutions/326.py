class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if x != dsu[x]:
                dsu[x] = find(dsu[x])
            return dsu[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            dsu[x] = y
            return True

        res = type_1 = type_2 = 0
        dsu, type_edges = list(range(n + 1)), [[], [], [], []]
        for t, u, v in edges:
            type_edges[t].append([u, v])
        for u, v in type_edges[3]:
            if union(u, v):
                type_1 += 1
                type_2 += 1
            else:
                res += 1
        dsu_bak = dsu[:]
        for u, v in type_edges[1]:
            if union(u, v):
                type_1 += 1
            else:
                res += 1
        dsu = dsu_bak
        for u, v in type_edges[2]:
            if union(u, v):
                type_2 += 1
            else:
                res += 1
        return res if type_1 == type_2 == n - 1 else -1
