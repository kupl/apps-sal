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

    def getSize(self, key):
        return self.d[self.findRoot(key)]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        Edges = []
        [heapq.heappush(Edges, (-e[0], e[1], e[2])) for e in edges]
        uf1 = UF()
        uf2 = UF()

        ttl = 0
        while len(Edges) != 0:
            t, src, dst = heapq.heappop(Edges)

            if t == -1:
                if uf1.findRoot(src) == uf1.findRoot(dst):
                    ttl += 1
                    continue
                else:
                    uf1.d[uf1.mergeRoot(src, dst)] -= 1
            if t == -2:
                if uf2.findRoot(src) == uf2.findRoot(dst):
                    ttl += 1
                    continue
                else:
                    uf2.d[uf2.mergeRoot(src, dst)] -= 1

            if t == -3:
                if uf1.findRoot(src) == uf1.findRoot(dst) and uf2.findRoot(src) == uf2.findRoot(dst):
                    ttl += 1
                    continue
                else:
                    uf1.d[uf1.mergeRoot(src, dst)] -= 1
                    uf2.d[uf2.mergeRoot(src, dst)] -= 1

        if uf1.d[1] != - n + 1 or uf2.d[1] != - n + 1:
            return -1

        return ttl
