class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (p1, s1) = (list(range(n + 1)), [1] * (n + 1))
        inc = 0

        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, size, x, y):
            (i, j) = (find(parent, x), find(parent, y))
            if size[i] < size[j]:
                parent[i] = j
                size[j] += size[i]
            else:
                parent[j] = i
                size[i] += size[j]
        for (t, u, v) in edges:
            if t == 3:
                (i, j) = (find(p1, u), find(p1, v))
                if i == j:
                    continue
                union(p1, s1, i, j)
                inc += 1
        (p2, s2) = (p1[:], s1[:])
        for (t, u, v) in edges:
            if t == 1:
                (i, j) = (find(p1, u), find(p1, v))
                if i == j:
                    continue
                union(p1, s1, i, j)
                inc += 1
            elif t == 2:
                (i, j) = (find(p2, u), find(p2, v))
                if i == j:
                    continue
                union(p2, s2, i, j)
                inc += 1
        return len(edges) - inc if max(s1) == n and max(s2) == n else -1
