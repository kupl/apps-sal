class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = [[i for i in range(n + 1)] for _ in range(4)]
        size = [[1 for i in range(n + 1)] for _ in range(4)]

        def find(x, t):
            if parent[t][x] != x:
                parent[t][x] = find(parent[t][x], t)
            return parent[t][x]

        def union(x, y, t):
            (xs, ys) = (find(x, t), find(y, t))
            if xs == ys:
                return False
            if size[t][xs] < size[t][ys]:
                (xs, ys) = (ys, xs)
            size[t][xs] += size[t][ys]
            parent[t][ys] = xs
            return True
        ans = 0
        for (t, u, v) in edges:
            if t != 3:
                continue
            union(u, v, 1)
            union(u, v, 2)
            if not union(u, v, 3):
                ans += 1
        for (t, u, v) in edges:
            if t != 1:
                continue
            if not union(u, v, 1):
                ans += 1
        for (t, u, v) in edges:
            if t != 2:
                continue
            if not union(u, v, 2):
                ans += 1
        for i in range(1, n + 1):
            for t in [1, 2]:
                if size[t][find(i, t)] != n:
                    return -1
        return ans
