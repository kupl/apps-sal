class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        t = [[] for _ in range(3)]
        for T, x, y in edges:
            t[T - 1].append([x - 1, y - 1])

        def root(cc, i):
            if cc[i] != i:
                cc[i] = root(cc, cc[i])
            return cc[i]

        def join(cc, i, j):
            ri = root(cc, i)
            rj = root(cc, j)
            if ri != rj:
                cc[ri] = rj
            return ri != rj

        ret = 0

        cc = [i for i in range(n)]
        cct = n
        for x, y in t[2]:
            if join(cc, x, y):
                cct -= 1
                ret += 1
                if cct == 1:
                    break

        ac = cc[:]
        bc = cc[:]
        acct = bcct = cct

        for x, y in t[0]:
            if join(ac, x, y):
                acct -= 1
                ret += 1
                if acct == 1:
                    break
        if acct != 1:
            return -1

        for x, y in t[1]:
            if join(bc, x, y):
                bcct -= 1
                ret += 1
                if bcct == 1:
                    break
        if bcct != 1:
            return -1

        return len(edges) - ret
