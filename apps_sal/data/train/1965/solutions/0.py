class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0 if n == 0 else -1
        p = [i for i in range(n)]

        def getP(ind):
            nonlocal p
            if p[ind] == ind:
                return ind
            else:
                res = getP(p[ind])
                p[ind] = res
                return res
        cnt = 0
        for (t, u, v) in edges:
            if t == 3:
                (pu, pv) = (getP(u - 1), getP(v - 1))
                if pu != pv:
                    p[pv] = pu
                    cnt += 1
        if cnt != n - 1:
            pa = list(p)
            for (t, u, v) in edges:
                if t == 1:
                    (pu, pv) = (getP(u - 1), getP(v - 1))
                    if pu != pv:
                        p[pv] = pu
                        cnt += 1
            targetP = getP(0)
            for v in range(n):
                if getP(v) != targetP:
                    return -1
            p = pa
            for (t, u, v) in edges:
                if t == 2:
                    (pu, pv) = (getP(u - 1), getP(v - 1))
                    if pu != pv:
                        p[pv] = pu
                        cnt += 1
            targetP = getP(0)
            for v in range(n):
                if getP(v) != targetP:
                    return -1
        return len(edges) - cnt
