class Solution:

    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:

        def union(UF, u, v):
            UF[find(UF, v)] = find(UF, u)

        def find(UF, u):
            if UF[u] != u:
                UF[u] = find(UF, UF[u])
            return UF[u]

        def check(UF, t):
            UF = UF.copy()
            for (tp, u, v) in e:
                if tp == t:
                    if find(UF, u) == find(UF, v):
                        self.ans += 1
                    else:
                        union(UF, u, v)
            return (len(set((find(UF, u) for u in UF))) == 1, UF)
        (self.ans, UF) = (0, {u: u for u in range(1, n + 1)})
        UF = check(UF, 3)[1]
        if not check(UF, 1)[0] or not check(UF, 2)[0]:
            return -1
        return self.ans
