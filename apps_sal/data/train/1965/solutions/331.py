class Solution:
    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        def union(UF, u, v):
            UF.setdefault(u, u)
            UF.setdefault(v, v)
            pu, pv = find(UF, u), find(UF, v)
            if pu != pv:
                UF[pv] = pu

        def find(UF, u):
            UF.setdefault(u, u)
            if UF[u] != u:
                UF[u] = find(UF, UF[u])
            return UF[u]

        def par_size(UF):
            return len(set(find(UF, u) for u in range(1, n + 1)))

        def check(UF, t):
            UF = UF.copy()
            for tp, u, v in e:
                if tp != t:
                    continue
                pu, pv = find(UF, u), find(UF, v)
                if pu == pv:
                    self.ans += 1
                else:
                    union(UF, u, v)
            return par_size(UF) == 1

        self.ans, UF = 0, {}
        for t, u, v in e:
            if t != 3:
                continue
            pu, pv = find(UF, u), find(UF, v)
            if pu == pv:
                self.ans += 1
            else:
                union(UF, u, v)

        if not check(UF, 1):
            return -1
        if not check(UF, 2):
            return -1
        return self.ans
