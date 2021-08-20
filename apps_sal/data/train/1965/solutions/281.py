class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(x):
            if fa[x] == x:
                return x
            fa[x] = find(fa[x])
            return fa[x]

        def merge(x, y):
            fx = find(x)
            fy = find(y)
            if fx != fy:
                fa[fx] = fy
                cnt[fy] = cnt[fx] + cnt[fy]
        fa = [i for i in range(n + 1)]
        cnt = [1 for i in range(n + 1)]
        ans = 0
        for edge in edges:
            if edge[0] == 3:
                (fx, fy) = (find(edge[1]), find(edge[2]))
                if fx != fy:
                    merge(fx, fy)
                    ans += 1
        fa_copy = [x for x in fa]
        for edge in edges:
            if edge[0] == 1:
                (fx, fy) = (find(edge[1]), find(edge[2]))
                if fx != fy:
                    merge(fx, fy)
                    ans += 1
        f0 = find(1)
        for i in range(1, n + 1):
            if find(i) != f0:
                return -1
        fa = [x for x in fa_copy]
        for edge in edges:
            if edge[0] == 2:
                (fx, fy) = (find(edge[1]), find(edge[2]))
                if fx != fy:
                    merge(fx, fy)
                    ans += 1
        f0 = find(1)
        for i in range(1, n + 1):
            if find(i) != f0:
                return -1
        return len(edges) - ans
