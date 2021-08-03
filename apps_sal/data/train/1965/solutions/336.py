class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            f[x] = y
            return True

        res, e1, e2 = 0, 0, 0

        for t, u, v in edges:
            if t == 3:
                if union(u, v):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1

        copy_f = f.copy()
        for t, u, v in edges:
            if t == 1:
                if union(u, v):
                    e1 += 1
                else:
                    res += 1

        f = copy_f
        for t, u, v in edges:
            if t == 2:
                if union(u, v):
                    e2 += 1
                else:
                    res += 1

        return res if e1 == e2 == n - 1 else -1
