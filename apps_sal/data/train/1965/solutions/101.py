class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        fa = [i for i in range(n + 1)]

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def uni(x, y):
            fx = find(x)
            fy = find(y)
            fa[fx] = fy
        res = 0
        A = 0
        B = 0
        for (t, u, v) in edges:
            if t == 3:
                fu = find(u)
                fv = find(v)
                if fu == fv:
                    res += 1
                else:
                    uni(u, v)
                    A += 1
                    B += 1
        fa_copy = fa[:]
        for (t, u, v) in edges:
            if t == 1:
                fu = find(u)
                fv = find(v)
                if fu == fv:
                    res += 1
                else:
                    uni(u, v)
                    A += 1
        fa = fa_copy
        for (t, u, v) in edges:
            if t == 2:
                fu = find(u)
                fv = find(v)
                if fu == fv:
                    res += 1
                else:
                    uni(u, v)
                    B += 1
        if A != n - 1 or B != n - 1:
            return -1
        return res
