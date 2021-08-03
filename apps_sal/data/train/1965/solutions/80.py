class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        p1 = list(range(n + 1))
        p2 = list(range(n + 1))

        def find(parents, node):
            if parents[node] != node:
                parents[node] = find(parents, parents[node])
            return parents[node]

        def union(parents, a, b):
            ra = find(parents, a)
            rb = find(parents, b)
            if ra != rb:
                parents[ra] = rb
                return True
            return False

        def count(parents, n):
            res = 0
            root = find(parents, 1)
            for i in range(n + 1):
                if find(parents, i) == root:
                    res += 1
            return res

        res = 0
        edges.sort(reverse=True)
        for t, u, v in edges:
            if t == 1 and not union(p1, u, v):
                res += 1
            if t == 2 and not union(p2, u, v):
                res += 1
            if t == 3:
                del1 = not union(p1, u, v)
                del2 = not union(p2, u, v)
                if (del1 and del2):
                    res += 1
        if count(p1, n) == n and count(p2, n) == n:
            return res
        return -1
