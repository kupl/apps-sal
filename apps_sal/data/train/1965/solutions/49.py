import heapq


class UF:
    def __init__(self):
        self.d = defaultdict(int)

    def findRoot(self, key):
        if self.d[key] > 0:
            self.d[key] = self.findRoot(self.d[key])
            return self.d[key]
        else:
            return key

    def mergeRoot(self, k1, k2):
        r1, r2 = self.findRoot(k1), self.findRoot(k2)
        if r1 != r2:
            r1, r2 = min(r1, r2), max(r1, r2)
            self.d[r1] += self.d[r2]
            self.d[r2] = r1
        return r1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        t12, t3 = [], []
        for e in edges:
            if e[0] == 3:
                t3.append(e)
            else:
                t12.append(e)

        uf1 = UF()
        uf2 = UF()
        uf1.d[1] = -1
        uf2.d[1] = -1
        ttl = 0
        for e in t3:
            if uf1.findRoot(e[1]) != uf1.findRoot(e[2]) or uf2.findRoot(e[1]) != uf2.findRoot(e[2]):
                uf1.d[uf1.mergeRoot(e[1], e[2])] -= 1
                uf2.d[uf2.mergeRoot(e[1], e[2])] -= 1
                ttl += 1

        for e in t12:
            if e[0] == 1 and uf1.findRoot(e[1]) != uf1.findRoot(e[2]):
                uf1.d[uf1.mergeRoot(e[1], e[2])] -= 1
            elif e[0] == 2 and uf2.findRoot(e[1]) != uf2.findRoot(e[2]):
                uf2.d[uf2.mergeRoot(e[1], e[2])] -= 1

        if uf1.d[1] != - n or uf2.d[1] != - n:
            return -1

        return len(edges) - 2 * n + 2 + ttl
