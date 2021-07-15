class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        class UF():
            def __init__(self, keys):
                self.uf = {}
                for key in keys:
                    self.uf[key] = key

            def find(self, x):
                if self.uf[x] == x:
                    return x
                ret = self.find(self.uf[x])
                self.uf[x] = ret
                return ret

            def union(self, x, y):
                xx = self.find(x)
                yy = self.find(y)
                self.uf[xx] = yy
        uf = UF(range(len(graph)))
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 1:
                    uf.union(i, j)
        ct = collections.Counter([uf.find(x) for x in range(len(graph))])
        ct2 = collections.Counter([uf.find(x) for x in initial])
        initial.sort()
        ret = initial[0]
        score = 0
        for idx in initial:
            parent = uf.find(idx)
            if ct2[parent] > 1:
                continue
            if ct[parent] > score:
                score = ct[parent]
                ret = idx
        return ret
