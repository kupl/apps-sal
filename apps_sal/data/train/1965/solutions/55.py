class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A, B, ans, m = list(), list(), 0, len(edges)
        ta, tb = set(), set()
        for i, (t, u, v) in enumerate(sorted(edges, reverse=True)):
            if t != 3:
                if (u, v, 3) in ta or (u, v, 3) in tb:
                    ans += 1
                    m -= 1
                elif t == 1:
                    ta.add((u, v, t))
                    A.append((u, v, i))
                else:
                    tb.add((u, v, t))
                    B.append((u, v, i))
            else:
                ta.add((u, v, t))
                A.append((u, v, i))
                tb.add((u, v, t))
                B.append((u, v, i))

        def mst(edges):
            p = list(range(n+1))
            ret = set()
            def find(x):
                if x != p[x]:
                    p[x] = find(p[x])
                return p[x]
            for u, v, i in edges:
                pu, pv = find(u), find(v)
                if pu != pv:
                    ret.add(i)
                    p[pu] = pv
            return ret if len(ret) == n-1 else None
        ta = mst(A)
        if ta is None:
            return -1
        tb = mst(B)
        if tb is None:
            return -1
        return ans + m - len(ta|tb)
