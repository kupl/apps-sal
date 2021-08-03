class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n + 1))
        rank = [0 for _ in range(n + 1)]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            id_x = find(x)
            id_y = find(y)
            if id_x == id_y:
                return 0
            if rank[id_x] >= rank[id_y]:
                if rank[id_x] == rank[id_y]:
                    rank[id_x] += 1
                parent[id_y] = id_x
            else:
                parent[id_x] = id_y
            return 1
        res = a = b = 0
        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    a += 1
                    b += 1
                else:
                    res += 1
        parent_, rank_ = parent[:], rank[:]
        for t, i, j in edges:
            if t == 1:
                if union(i, j):
                    a += 1
                else:
                    res += 1
        parent, rank = parent_, rank_
        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    b += 1
                else:
                    res += 1
        return res if (a == n - 1 and b == n - 1) else -1
